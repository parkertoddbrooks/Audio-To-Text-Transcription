# Audio-To-Text Transcription Tool

This tool allows you to transcribe audio files to text using either the free Google Speech Recognition service or the paid Google Cloud Speech-to-Text API. It also offers post-processing capabilities using Claude Opus 3 for enhanced formatting and error correction.

## Features

- Support for multiple audio formats: MP3, WAV, M4A, AAC, FLAC, OGG, WMA, AIFF, AIF, AMR
- Free version for transcribing short audio clips
- Paid version for transcribing longer audio files with improved accuracy (requires Google Cloud API key)
- Efficient processing of long audio files using chunking and parallel processing
- User-friendly command-line interface with interactive prompts
- Automatic audio format conversion when necessary
- Display of word count, audio duration, and confidence score for transcriptions (where applicable)
- Option to save transcriptions as text or markdown files
- Intelligent file naming to avoid overwriting existing files
- Real-time progress reporting for long audio files
- Post-processing option using Claude Opus 3 for improved readability and error correction

## Requirements

- Python 3.6 or higher
- FFmpeg (for audio format conversion)
- Google Cloud account and credentials (for paid version)
- Anthropic API key (for Claude post-processing)

## Installation

1. Clone this repository or download the project files.

2. Install the required Python libraries:

   ```
   pip install -r requirements.txt
   ```

3. Install FFmpeg:
   - On macOS (using Homebrew): `brew install ffmpeg`
   - On Ubuntu or Debian: `sudo apt-get install ffmpeg`
   - On Windows, download the FFmpeg binaries from the official website and add them to your system PATH.

4. For the paid version, follow the setup instructions in the [google-cloud-api-setup.md](google-cloud-api-setup.md) file.

5. For Claude post-processing, create a .env file in the project root and add your Anthropic API key:
   ```
   CLAUDE_API_KEY=your_api_key_here
   ```

## Usage

Run the main script from the command line:

```
python3 main.py
```

Follow the interactive prompts to:
1. Choose between the free version (for short audio clips) and the paid version (for longer audio files).
2. Provide the path to your audio file.
3. Save the transcription (optional) and choose the output format (text or markdown).
4. Optionally post-process the transcription using Claude Opus 3.

The script will:
1. Convert the audio file to the required format if necessary.
2. For longer files (paid version), split the audio into chunks for efficient processing.
3. Transcribe the audio using the selected service, with parallel processing for longer files.
4. Display the transcription, word count, audio duration, and confidence score (where applicable).
5. Show real-time progress for longer files being processed in chunks.
6. Optionally save the transcription to a file in the specified directory.
7. If chosen, post-process the transcription using Claude Opus 3 for improved formatting and error correction.

## Notes

- The free version is limited to short audio clips (typically 10-15 seconds) due to API constraints.
- The paid version supports longer audio files with improved accuracy, using the latest Google Cloud Speech-to-Text API (v1p1beta1).
- Long audio files are automatically split into chunks and processed in parallel for faster transcription.
- Temporary files created during processing are automatically cleaned up.
- When saving transcriptions, the tool checks for existing files and increments the filename (e.g., filename-01, filename-02) to avoid overwriting.
- Claude post-processing is performed in chunks for long transcriptions to stay within API limits.

## Troubleshooting

- Ensure FFmpeg is correctly installed and accessible in your system PATH.
- Verify that you have an active internet connection, as both versions use online speech recognition services.
- For the paid version, make sure your Google Cloud credentials are correctly set up as described in the [google-cloud-api-setup.md](google-cloud-api-setup.md) file.
- For Claude post-processing, ensure your Anthropic API key is correctly set in the .env file.
- If you encounter "Invalid audio file" errors, check that your audio file is not corrupted and is in a supported format.
- For very large audio files, ensure you have sufficient disk space for temporary files and chunked processing.
- If you experience API quota issues with the paid version or Claude post-processing, check your respective API consoles for any limits or billing issues.

If you encounter any other issues or have questions, please open an issue in this repository.

## Future Improvements

- Implement batch processing for multiple audio files
- Develop a web-based user interface for easier use
- Add support for more languages and dialects
- Implement a caching system to avoid reprocessing of previously transcribed audio
- Explore options for improving transcription accuracy through custom language models
- Develop a comprehensive logging system for better debugging and performance analysis
- Enhance the Claude post-processing feature with more advanced formatting options
- Implement a progress bar for long-running processes

We welcome contributions and suggestions to improve this tool.