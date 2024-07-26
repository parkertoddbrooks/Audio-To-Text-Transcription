(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text % python3 main.py
╭──────────────────────────────────────────────────────────────────── Welcome ────────────────────────────────────────────────────────────────────╮
│ Welcome to the Audio-To-Text Transcription Tool!                                                                                                │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
1. Free version (limited to short audio clips)
2. Paid version (supports longer audio files, requires Google Cloud API key)
3. Exit
Please enter your choice (1, 2, or 3): 1
Path to audio file: /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/audio/test-git-ignore/test-file-short-02.m4a 
╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Running Free Version                                                                                                                            │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
^CTraceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/main.py", line 60, in <module>
    main()
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/main.py", line 48, in main
    result = subprocess.run([sys.executable, script_path, audio_file], capture_output=True, text=True, check=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/subprocess.py", line 1209, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/subprocess.py", line 2115, in _communicate
    ready = selector.select(timeout)
            ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/selectors.py", line 415, in select
    fd_event_list = self._selector.poll(timeout)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt

(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text % 
