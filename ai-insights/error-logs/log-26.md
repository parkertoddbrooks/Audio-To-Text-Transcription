(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip install --upgrade pip setuptools 
Requirement already satisfied: pip in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (24.1.2)
Collecting setuptools
  Downloading setuptools-71.1.0-py3-none-any.whl.metadata (6.6 kB)
Downloading setuptools-71.1.0-py3-none-any.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 18.1 MB/s eta 0:00:00
Installing collected packages: setuptools
Successfully installed setuptools-71.1.0
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip uninstall google-cloud-speech
Found existing installation: google-cloud-speech 2.21.0
Uninstalling google-cloud-speech-2.21.0:
  Would remove:
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech/*
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1/*
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/*
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v2/*
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google_cloud_speech-2.21.0-py3.9-nspkg.pth
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google_cloud_speech-2.21.0.dist-info/*
  Would not remove (might be manually added):
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v2/__init__ 2.py
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v2/gapic_metadata 2.json
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v2/gapic_version 2.py
    /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v2/py 2.typed
Proceed (Y/n)? y
  Successfully uninstalled google-cloud-speech-2.21.0
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip install google-cloud-speech
Collecting google-cloud-speech
  Using cached google_cloud_speech-2.26.1-py2.py3-none-any.whl.metadata (5.2 kB)
Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (2.19.1)
Requirement already satisfied: google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-cloud-speech) (2.32.0)
Requirement already satisfied: proto-plus<2.0.0dev,>=1.22.3 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-cloud-speech) (1.24.0)
Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0dev,>=3.20.2 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-cloud-speech) (4.25.3)
Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (1.63.2)
Requirement already satisfied: requests<3.0.0.dev0,>=2.18.0 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (2.32.3)
Requirement already satisfied: grpcio<2.0dev,>=1.33.2 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (1.65.0)
Requirement already satisfied: grpcio-status<2.0.dev0,>=1.33.2 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (1.62.2)
Requirement already satisfied: cachetools<6.0,>=2.0.0 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1->google-cloud-speech) (5.3.3)
Requirement already satisfied: pyasn1-modules>=0.2.1 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1->google-cloud-speech) (0.4.0)
Requirement already satisfied: rsa<5,>=3.1.4 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1->google-cloud-speech) (4.9)
Requirement already satisfied: pyasn1<0.7.0,>=0.4.6 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from pyasn1-modules>=0.2.1->google-auth!=2.24.0,!=2.25.0,<3.0.0dev,>=2.14.1->google-cloud-speech) (0.6.0)
Requirement already satisfied: charset-normalizer<4,>=2 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (3.3.2)
Requirement already satisfied: idna<4,>=2.5 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (3.7)
Requirement already satisfied: urllib3<3,>=1.21.1 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (2.2.2)
Requirement already satisfied: certifi>=2017.4.17 in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-api-core[grpc]!=2.0.*,!=2.1.*,!=2.10.*,!=2.2.*,!=2.3.*,!=2.4.*,!=2.5.*,!=2.6.*,!=2.7.*,!=2.8.*,!=2.9.*,<3.0.0dev,>=1.34.1->google-cloud-speech) (2024.7.4)
Using cached google_cloud_speech-2.26.1-py2.py3-none-any.whl (289 kB)
Installing collected packages: google-cloud-speech
Successfully installed google-cloud-speech-2.26.1
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip install --upgrade protobuf 
Requirement already satisfied: protobuf in /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages (4.25.3)
Collecting protobuf
  Using cached protobuf-5.27.2-cp38-abi3-macosx_10_9_universal2.whl.metadata (592 bytes)
Using cached protobuf-5.27.2-cp38-abi3-macosx_10_9_universal2.whl (412 kB)
Installing collected packages: protobuf
  Attempting uninstall: protobuf
    Found existing installation: protobuf 4.25.3
    Uninstalling protobuf-4.25.3:
      Successfully uninstalled protobuf-4.25.3
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
google-cloud-audit-log 0.2.5 requires protobuf!=3.20.0,!=3.20.1,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5, but you have protobuf 5.27.2 which is incompatible.
google-cloud-logging 3.10.0 requires protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.19.5, but you have protobuf 5.27.2 which is incompatible.
Successfully installed protobuf-5.27.2
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % 
