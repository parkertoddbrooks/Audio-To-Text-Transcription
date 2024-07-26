Choose an option:
1. Free version (limited to short audio clips)
2. Paid version (supports longer audio files, requires Google Cloud API key)
3. Process existing text file
4. Exit
Enter your choice: 2
Path to audio file: /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/dev-tests/Audio/test-file-long.mp3 
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Processing audio file...                                                                                                                                                                                              │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Processing audio file...
Converting audio to WAV format...
Error during audio processing: Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/main.py", line 224, in <module>
    main()
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/main.py", line 177, in main
    result = process_audio_paid(audio_file)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/src/google_api.py", line 62, in process_audio
    client = speech.SpeechClient()
             ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/speech/client.py", line 459, in __init__
    self._transport = Transport(
                      ^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/speech/transports/grpc.py", line 153, in __init__
    super().__init__(
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/speech/transports/base.py", line 101, in __init__
    credentials, _ = google.auth.default(
                     ^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/auth/_default.py", line 691, in default
    raise exceptions.DefaultCredentialsError(_CLOUD_SDK_MISSING_CREDENTIALS)
google.auth.exceptions.DefaultCredentialsError: Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % 
