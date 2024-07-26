(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % git reflog expire --expire=now --all && git gc --prune=now --aggressive
Enumerating objects: 183, done.
Counting objects: 100% (183/183), done.
Delta compression using up to 16 threads
Compressing objects: 100% (179/179), done.
Writing objects: 100% (183/183), done.
Total 183 (delta 95), reused 0 (delta 0), pack-reused 0
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % git push git@github.com:parkertoddbrooks/Audio-To-Text-Transcription.git --force --all
Enumerating objects: 182, done.
Counting objects: 100% (182/182), done.
Delta compression using up to 16 threads
Compressing objects: 100% (83/83), done.
Writing objects: 100% (182/182), 17.40 MiB | 3.97 MiB/s, done.
Total 182 (delta 95), reused 182 (delta 95), pack-reused 0
remote: Resolving deltas: 100% (95/95), done.
remote: error: GH013: Repository rule violations found for refs/heads/main.
remote: 
remote: - GITHUB PUSH PROTECTION
remote:   —————————————————————————————————————————
remote:     Resolve the following violations before pushing again
remote: 
remote:     - Push cannot contain secrets
remote: 
remote:     
remote:      (?) Learn how to resolve a blocked push
remote:      https://docs.github.com/code-security/secret-scanning/pushing-a-branch-blocked-by-push-protection
remote:     
remote:     
remote:       —— Anthropic API Key —————————————————————————————————
remote:        locations:
remote:          - commit: 5011e737b550313377ed3e440a3cb7e73261c78c
remote:            path: .env:1
remote:          - commit: 5011e737b550313377ed3e440a3cb7e73261c78c
remote:            path: ai-insights/dev-summaries/git-ignore/cli-dump-v07.md:3304
remote:     
remote:        (?) To push, remove secret from commit(s) or follow this URL to allow the secret.
remote:        https://github.com/parkertoddbrooks/Audio-To-Text-Transcription/security/secret-scanning/unblock-secret/2jnWppAlDM1eisgFw5irWc4NUnV
remote:     
remote: 
remote: 
To github.com:parkertoddbrooks/Audio-To-Text-Transcription.git
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'github.com:parkertoddbrooks/Audio-To-Text-Transcription.git'
(audio-to-text-venv) parker@PxB-MBP-16 Audio-To-Text-Transcription % 
