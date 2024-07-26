(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % which ffmpeg
/usr/local/bin/ffmpeg
(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % which ffprobe
ffprobe not found
(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % brew install ffmpeg
Warning: ffmpeg 7.0.1 is already installed, it's just not linked.
To link this version, run:
  brew link ffmpeg
(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % brew link ffmpeg
Linking /usr/local/Cellar/ffmpeg/7.0.1... 
Error: Could not symlink bin/ffmpeg
Target /usr/local/bin/ffmpeg
already exists. You may want to remove it:
  rm '/usr/local/bin/ffmpeg'

To force the link and overwrite all conflicting files:
  brew link --overwrite ffmpeg

To list all files that would be deleted:
  brew link --overwrite ffmpeg --dry-run
(cli-dev-venv) parker@PxB-MBP-16 Audio-To-Text % which ffprobe
ffprobe not found

