(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text %  python3 main.py
╭───────────────────────────────────────────────────────────────────────────────── Welcome ─────────────────────────────────────────────────────────────────────────────────╮
│ Welcome to the Audio-To-Text Transcription Tool!                                                                                                                          │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Choose an option:
1. Free version (limited to short audio clips)
2. Paid version (supports longer audio files, requires Google Cloud API key)
3. Exit
Enter your choice: 2
Path to audio file: /Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/dev-tests-git-ignore/Audio/test-file-long.mp3 
╭───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ Processing audio file...                                                                                                                                                  │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
Processing audio file...
Converting audio to WAV format...
Conversion complete.
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1720741777.896225 2383031 config.cc:230] gRPC experiments enabled: call_status_override_on_cancellation, event_engine_dns, event_engine_listener, http2_stats_fix, monitoring_experiment, pick_first_new, trace_record_callops, work_serializer_clears_time_cache, work_serializer_dispatch
I0000 00:00:1720741777.906874 2383031 check_gcp_environment_no_op.cc:29] ALTS: Platforms other than Linux and Windows are not supported
Processing chunk 1/11...
Error during audio processing: 400 Request payload size exceeds the limit: 10485760 bytes.
Traceback (most recent call last):
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/main.py", line 110, in <module>
    main()
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/main.py", line 74, in main
    result = process_audio_paid(audio_file)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/src/google_api.py", line 60, in process_audio
    chunk_transcription = transcribe_audio_chunk(client, chunk)
                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/claude-engineer/_Projects/Audio-To-Text/src/google_api.py", line 38, in transcribe_audio_chunk
    response = client.recognize(config=config, audio=audio)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/cloud/speech_v1/services/speech/client.py", line 811, in recognize
    response = rpc(
               ^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/gapic_v1/method.py", line 131, in __call__
    return wrapped_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/retry/retry_unary.py", line 293, in retry_wrapped_func
    return retry_target(
           ^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/retry/retry_unary.py", line 153, in retry_target
    _retry_error_helper(
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/retry/retry_base.py", line 212, in _retry_error_helper
    raise final_exc from source_exc
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/retry/retry_unary.py", line 144, in retry_target
    result = target()
             ^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/timeout.py", line 120, in func_with_timeout
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/parker/Documents/dev/venvs/audio-to-text-venv/lib/python3.12/site-packages/google/api_core/grpc_helpers.py", line 78, in error_remapped_callable
    raise exceptions.from_grpc_error(exc) from exc
google.api_core.exceptions.InvalidArgument: 400 Request payload size exceeds the limit: 10485760 bytes.
I0000 00:00:1720741784.953797 2383334 tcp_posix.cc:809] IOMGR endpoint shutdown
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text % 
