(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip install --no-cache-dir --upgrade -r requirements.txt
Requirement already satisfied: anthropic==0.3.6 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from -r requirements.txt (line 1)) (0.3.6)
Requirement already satisfied: anyio==4.4.0 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from -r requirements.txt (line 2)) (4.4.0)
Requirement already satisfied: google-cloud-speech==2.21.0 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from -r requirements.txt (line 3)) (2.21.0)
Requirement already satisfied: protobuf==3.20.3 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from -r requirements.txt (line 4)) (3.20.3)
Requirement already satisfied: pydub==0.25.1 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from -r requirements.txt (line 5)) (0.25.1)
Requirement already satisfied: python-dotenv==1.0.0 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from -r requirements.txt (line 6)) (1.0.0)
Requirement already satisfied: rich==13.4.2 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from -r requirements.txt (line 7)) (13.4.2)
Requirement already satisfied: SpeechRecognition==3.10.0 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from -r requirements.txt (line 8)) (3.10.0)
INFO: pip is looking at multiple versions of anthropic to determine which version is compatible with other requirements. This could take a while.
Collecting anthropic==0.3.6 (from -r requirements.txt (line 1))
  Downloading anthropic-0.3.6-py3-none-any.whl.metadata (10 kB)
ERROR: Cannot install -r requirements.txt (line 1), anthropic==0.3.6 and anyio==4.4.0 because these package versions have conflicting dependencies.

The conflict is caused by:
    The user requested anyio==4.4.0
    anthropic 0.3.6 depends on anyio<4 and >=3.5.0
    The user requested anyio==4.4.0
    anthropic 0.3.6 depends on anyio<4 and >=3.5.0

To fix this you could try to:
1. loosen the range of package versions you've specified
2. remove package versions to allow pip to attempt to solve the dependency conflict

ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % 

