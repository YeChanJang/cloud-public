FROM vllm/vllm-openai:latest

# Sample image for blog/demo use.
# For production, replace latest with a tested and pinned vLLM image tag.

ENV MODEL_ID="Qwen/Qwen2.5-7B-Instruct"
ENV HOST="0.0.0.0"
ENV PORT="8000"
ENV MAX_MODEL_LEN="4096"
ENV GPU_MEMORY_UTILIZATION="0.90"
ENV VLLM_API_KEY="dummy-key-for-vllm"

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]