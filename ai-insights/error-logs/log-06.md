(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % python3 main.py
Welcome to Audio-To-Text Transcription Tool
1. Free version (limited to short audio clips)
2. Paid version (supports longer audio files, requires Google Cloud API key)
Please enter your choice (1 or 2): 2
Debug: User chose option 2
Path to file: /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/audio/file.mp3 
Debug: User entered file path: /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/audio/file.mp3
Debug: About to run script: /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/src/main-api-key-needed.py
Debug: With audio file: /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/audio/file.mp3
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/src/main-api-key-needed.py", line 3, in <module>
    from google.cloud import speech
ModuleNotFoundError: No module named 'google'
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/main.py", line 35, in <module>
    main()
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/main.py", line 31, in main
    subprocess.run([sys.executable, script_path, audio_file], check=True)
  File "/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/subprocess.py", line 571, in run
    raise CalledProcessError(retcode, process.args,
subprocess.CalledProcessError: Command '['/Users/parker/Documents/dev/venvs/cli-dev-venv/bin/python3', '/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/src/main-api-key-needed.py', '/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/audio/file.mp3']' returned non-zero exit status 1.
(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % 
