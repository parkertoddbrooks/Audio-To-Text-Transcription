(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text %  python3 main.py                           
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/main.py", line 14, in <module>
    from src.google_api import process_audio as process_audio_paid
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/src/google_api.py", line 22, in <module>
    logger.setLevel(logging.ERROR)
    ^^^^^^^^^^^^^^^
AttributeError: 'Logger' object has no attribute 'setLevel'
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text % 
