(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % py main.py
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/main.py", line 15, in <module>
    from src.google_api import process_audio as process_audio_paid
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/src/google_api.py", line 1, in <module>
    from google.cloud import speech_v1p1beta1 as speech
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/__init__.py", line 21, in <module>
    from .services.adaptation import AdaptationClient
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/adaptation/__init__.py", line 16, in <module>
    from .client import AdaptationClient
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1p1beta1/services/adaptation/client.py", line 35, in <module>
    from google.api_core import exceptions as core_exceptions
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/exceptions.py", line 29, in <module>
    from google.rpc import error_details_pb2
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/rpc/error_details_pb2.py", line 22, in <module>
    from google.protobuf import symbol_database as _symbol_database
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/protobuf/symbol_database.py", line 41, in <module>
    from google.protobuf import message_factory
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/protobuf/message_factory.py", line 28, in <module>
    from google.protobuf.pyext import cpp_message as message_impl  # pylint: disable=g-import-not-at-top
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'google.protobuf.pyext'
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % 

