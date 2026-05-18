#!/usr/bin/env bash
set -euo pipefail

curl http://localhost:11434/api/generate \
  -d '{
    "model": "gemma3",
    "prompt": "Explain what Ollama does in one sentence.",
    "stream": false
  }'
