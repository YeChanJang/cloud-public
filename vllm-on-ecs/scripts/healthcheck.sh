#!/usr/bin/env bash
set -euo pipefail

BASE_URL="${VLLM_BASE_URL:-http://localhost:8000}"

curl -fsS "${BASE_URL}/health"
echo "vLLM health check passed: ${BASE_URL}"
