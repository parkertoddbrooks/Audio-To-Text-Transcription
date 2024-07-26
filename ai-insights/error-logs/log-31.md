(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip show anyio   
Name: anyio
Version: 3.7.1
Summary: High level compatibility layer for multiple asynchronous event loop implementations
Home-page: 
Author: 
Author-email: Alex Grönholm <alex.gronholm@nextday.fi>
License: MIT
Location: /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages
Requires: idna, sniffio
Required-by: anthropic, httpx
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip show anthropic
Name: anthropic
Version: 0.3.6
Summary: Client library for the anthropic API
Home-page: https://github.com/anthropics/anthropic-sdk-python
Author: Anthropic
Author-email: support@anthropic.com
License: MIT
Location: /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages
Requires: anyio, distro, httpx, pydantic, tokenizers, typing-extensions
Required-by: 
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip show google-cloud-speech    
Name: google-cloud-speech
Version: 2.21.0
Summary: Google Cloud Speech API client library
Home-page: https://github.com/googleapis/python-speech
Author: Google LLC
Author-email: googleapis-packages@google.com
License: Apache 2.0
Location: /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages
Requires: google-api-core, proto-plus, protobuf
Required-by: 
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip show protobuf   
Name: protobuf
Version: 3.20.3
Summary: Protocol Buffers
Home-page: https://developers.google.com/protocol-buffers/
Author: 
Author-email: 
License: BSD-3-Clause
Location: /Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages
Requires: 
Required-by: google-api-core, google-cloud-appengine-logging, google-cloud-audit-log, google-cloud-logging, google-cloud-speech, googleapis-common-protos, grpc-google-iam-v1, grpcio-status, proto-plus
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % pip list  
Package                        Version
------------------------------ --------
annotated-types                0.7.0
anthropic                      0.3.6
anyio                          3.7.1
cachetools                     5.3.3
certifi                        2024.7.4
charset-normalizer             3.3.2
distro                         1.9.0
filelock                       3.15.4
fsspec                         2024.6.1
google-api-core                1.34.1
google-auth                    2.32.0
google-cloud-appengine-logging 1.4.4
google-cloud-audit-log         0.2.5
google-cloud-core              2.4.1
google-cloud-logging           3.10.0
google-cloud-speech            2.21.0
googleapis-common-protos       1.63.2
grpc-google-iam-v1             0.13.1
grpcio                         1.65.0
grpcio-status                  1.48.2
h11                            0.14.0
httpcore                       1.0.5
httpx                          0.27.0
huggingface-hub                0.23.4
idna                           3.7
jiter                          0.5.0
markdown-it-py                 3.0.0
mdurl                          0.1.2
packaging                      24.1
pip                            24.1.2
proto-plus                     1.24.0
protobuf                       3.20.3
pyasn1                         0.6.0
pyasn1_modules                 0.4.0
pydantic                       1.10.17
pydantic_core                  2.20.1
pydub                          0.25.1
Pygments                       2.18.0
python-dotenv                  1.0.0
PyYAML                         6.0.1
requests                       2.32.3
rich                           13.4.2
rsa                            4.9
setuptools                     71.1.0
sniffio                        1.3.1
SpeechRecognition              3.10.0
tokenizers                     0.19.1
tqdm                           4.66.4
typing_extensions              4.12.2
urllib3                        2.2.2
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % cat requirements.txt  
SpeechRecognition==3.10.0
pydub==0.25.1
google-cloud-speech==2.21.0
rich==13.4.2                                                                                                                                                                                                   
python-dotenv==1.0.0
anthropic==0.3.6 
protobuf==3.20.3%                                                                                                                                                                                                        (audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % python --version
Python 3.12.4
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % 
