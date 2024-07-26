(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % py main.py                                              
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/main.py", line 15, in <module>
    from src.google_api import process_audio as process_audio_paid
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/src/google_api.py", line 1, in <module>
    from google.cloud import speech_v1p1beta1 as speech
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/__init__.py", line 23, in <module>
    from .services.speech import SpeechClient
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/speech/__init__.py", line 16, in <module>
    from .client import SpeechClient
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/speech/client.py", line 57, in <module>
    from .transports.base import SpeechTransport, DEFAULT_CLIENT_INFO
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/speech/transports/__init__.py", line 19, in <module>
    from .base import SpeechTransport
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/speech/transports/base.py", line 26, in <module>
    from google.api_core import operations_v1
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/operations_v1/__init__.py", line 17, in <module>
    from google.api_core.operations_v1.abstract_operations_client import AbstractOperationsClient
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/operations_v1/abstract_operations_client.py", line 17, in <module>
    from distutils import util
ModuleNotFoundError: No module named 'distutils'
