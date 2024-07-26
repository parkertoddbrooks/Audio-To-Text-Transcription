(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % python3 main.py /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/file.mp3
Warning: FFprobe not found at /usr/local/bin/ffprobe
Audio conversion may not work properly.
Converting audio to WAV format...
/Users/parker/Documents/dev/venvs/cli-dev-venv/lib/python3.12/site-packages/pydub/utils.py:198: RuntimeWarning: Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work
  warn("Couldn't find ffprobe or avprobe - defaulting to ffprobe, but may not work", RuntimeWarning)
Error during conversion: [Errno 2] No such file or directory: 'ffprobe'
Make sure FFmpeg and FFprobe are correctly installed.
(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % 
