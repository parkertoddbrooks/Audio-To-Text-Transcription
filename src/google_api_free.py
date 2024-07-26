import speech_recognition as sr
from pydub import AudioSegment
import os
import tempfile
import wave

def convert_to_wav(input_file):
    print("DEBUG: Starting audio conversion...")
    try:
        audio = AudioSegment.from_file(input_file)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_wav:
            audio.export(temp_wav.name, format="wav")
        print("DEBUG: Audio conversion complete.")
        return temp_wav.name
    except Exception as e:
        print(f"ERROR: Audio conversion failed - {str(e)}")
        raise

def get_audio_duration(wav_file):
    print("DEBUG: Getting audio duration...")
    try:
        with wave.open(wav_file, 'rb') as wav_file:
            frames = wav_file.getnframes()
            rate = wav_file.getframerate()
            duration = frames / float(rate)
        print(f"DEBUG: Audio duration: {duration:.2f} seconds")
        return duration
    except Exception as e:
        print(f"ERROR: Failed to get audio duration - {str(e)}")
        raise

def transcribe_audio(wav_file):
    print("DEBUG: Starting transcription...")
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(wav_file) as source:
            audio = recognizer.record(source)
        
        transcription = recognizer.recognize_google(audio, show_all=True)
        if not transcription:
            print("DEBUG: No transcription result.")
            return None, None
        best_result = transcription['alternative'][0]
        print("DEBUG: Transcription successful.")
        return best_result['transcript'], best_result.get('confidence', None)
    except sr.UnknownValueError:
        print("ERROR: Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"ERROR: Could not request results from Google Speech Recognition service - {str(e)}")
    except Exception as e:
        print(f"ERROR: Unexpected error during transcription - {str(e)}")
    return None, None

def process_audio(input_file):
    temp_wav_file = None
    try:
        temp_wav_file = convert_to_wav(input_file)
        duration = get_audio_duration(temp_wav_file)
        transcription, confidence = transcribe_audio(temp_wav_file)

        if transcription:
            word_count = len(transcription.split())
            return {
                "transcription": transcription,
                "word_count": word_count,
                "duration": duration,
                "confidence": confidence
            }
        else:
            return None
    except Exception as e:
        print(f"ERROR: An unexpected error occurred - {str(e)}")
        return None
    finally:
        if temp_wav_file and os.path.exists(temp_wav_file):
            os.remove(temp_wav_file)

if __name__ == "__main__":
    # This block is for testing purposes only
    import sys
    if len(sys.argv) > 1:
        result = process_audio(sys.argv[1])
        if result:
            print(f"\nTranscription: {result['transcription']}")
            print(f"Word count: {result['word_count']}")
            print(f"Audio duration: {result['duration']:.2f} seconds")
            if result['confidence']:
                print(f"Confidence: {result['confidence']:.2f}")
        else:
            print("Transcription failed.")