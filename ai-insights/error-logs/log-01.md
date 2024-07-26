(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % python3 main.py                    
/Users/parker/Documents/dev/venvs/cli-dev-venv/lib/python3.12/site-packages/pydub/utils.py:198: RuntimeWarning: Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work
  warn("Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", RuntimeWarning)
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/main.py", line 5, in <module>
    audio = AudioSegment.from_mp3("file.mp3")
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/cli-dev-venv/lib/python3.12/site-packages/pydub/audio_segment.py", line 796, in from_mp3
    return cls.from_file(file, 'mp3', parameters=parameters)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/cli-dev-venv/lib/python3.12/site-packages/pydub/audio_segment.py", line 728, in from_file
    info = mediainfo_json(orig_file, read_ahead_limit=read_ahead_limit)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/cli-dev-venv/lib/python3.12/site-packages/pydub/utils.py", line 274, in mediainfo_json
    res = Popen(command, stdin=stdin_parameter, stdout=PIPE, stderr=PIPE)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/subprocess.py", line 1026, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/local/Cellar/python@3.12/3.12.4/Frameworks/Python.framework/Versions/3.12/lib/python3.12/subprocess.py", line 1955, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'ffprobe'
(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % python3 main.py /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/file.mp3
Converting audio to WAV format...
/Users/parker/Documents/dev/venvs/cli-dev-venv/lib/python3.12/site-packages/pydub/utils.py:198: RuntimeWarning: Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work
  warn("Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", RuntimeWarning)
Error during conversion: [Errno 2] No such file or directory: 'ffprobe'
(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % 

