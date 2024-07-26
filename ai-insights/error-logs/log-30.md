(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % py main.py
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text-Transcription/main.py", line 6, in <module>
    import anthropic
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/anthropic/__init__.py", line 3, in <module>
    from . import types
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/anthropic/types/__init__.py", line 5, in <module>
    from .usage import Usage as Usage
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/anthropic/types/usage.py", line 5, in <module>
    from .._models import BaseModel
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/anthropic/_models.py", line 36, in <module>
    from ._utils import (
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/anthropic/_utils/__init__.py", line 1, in <module>
    from ._sync import asyncify as asyncify
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/anthropic/_utils/_sync.py", line 7, in <module>
    import anyio
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/anyio/__init__.py", line 106, in <module>
    from ._core._sockets import (
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/anyio/_core/_sockets.py", line 22, in <module>
    from ..streams.stapled import MultiListener
ModuleNotFoundError: No module named 'anyio.streams'
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % 
