from google.cloud import speech_v1p1beta1 as speech
import io
import os
from pydub import AudioSegment
from concurrent.futures import ThreadPoolExecutor, as_completed
import tempfile
import logging

# Suppress warnings from gRPC and Abseil
logging.getLogger('absl').setLevel(logging.ERROR)
logging.getLogger('grpc').setLevel(logging.ERROR)
os.environ['GRPC_PYTHON_LOG_LEVEL'] = 'error'

# Suppress gRPC experiments output
os.environ['GRPC_VERBOSITY'] = 'ERROR'
os.environ['GRPC_TRACE'] = 'none'

# Suppress Google Cloud logging
logging.getLogger('google').setLevel(logging.ERROR)
logging.getLogger('google.cloud').setLevel(logging.ERROR)

def convert_to_wav(input_file):
    print("Converting audio to WAV format...")
    try:
        audio = AudioSegment.from_file(input_file)
        audio = audio.set_channels(1).set_frame_rate(16000)  # Mono, 16kHz
        return audio
    except Exception as e:
        print(f"Error during conversion: {e}")
        raise

def transcribe_chunk(client, audio_chunk, chunk_index):
    print(f"Processing chunk {chunk_index}...")
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio_file:
        audio_chunk.export(temp_audio_file.name, format="wav")

    with io.open(temp_audio_file.name, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_automatic_punctuation=True,
    )

    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result()

    os.unlink(temp_audio_file.name)

    return ' '.join(result.alternatives[0].transcript for result in response.results)

def process_audio(input_file):
    print("Processing audio file...")
    try:
        audio = convert_to_wav(input_file)
        chunk_length_ms = 45000  # 45 seconds
        chunks = [audio[i:i+chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
        
        client = speech.SpeechClient()
        transcription = ""
        total_chunks = len(chunks)

        with ThreadPoolExecutor(max_workers=5) as executor:
            future_to_chunk = {executor.submit(transcribe_chunk, client, chunk, i): i for i, chunk in enumerate(chunks)}
            for future in as_completed(future_to_chunk):
                chunk_index = future_to_chunk[future]
                try:
                    chunk_transcription = future.result()
                    transcription += chunk_transcription + " "
                    print(f"Processed chunk {chunk_index + 1}/{total_chunks}")
                except Exception as e:
                    print(f"Error processing chunk {chunk_index}: {str(e)}")

        transcription = transcription.strip()
        word_count = len(transcription.split())
        duration = len(audio) / 1000.0  # Convert milliseconds to seconds
        
        result = {
            'transcription': transcription,
            'word_count': word_count,
            'duration': duration,
            'confidence': None  # We don't have an overall confidence score
        }
        
        return result
    except Exception as e:
        print(f"Error during audio processing: {e}")
        raise

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Transcribe audio files to text using Google Cloud Speech-to-Text API.")
    parser.add_argument("input_file", help="Path to the input audio file")
    args = parser.parse_args()

    try:
        result = process_audio(args.input_file)
        print("\nTranscription:", result['transcription'])
        print(f"Word count: {result['word_count']}")
        print(f"Audio duration: {result['duration']:.2f} seconds")
    except Exception as e:
        print(f"Error: {e}")