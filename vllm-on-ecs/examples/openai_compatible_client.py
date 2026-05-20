from __future__ import annotations

import os
from openai import OpenAI

base_url = os.getenv("VLLM_BASE_URL", "http://localhost:8000/v1")
api_key = os.getenv("OPENAI_API_KEY", "dummy-key-for-vllm")
model = os.getenv("MODEL_ID", "Qwen/Qwen2.5-7B-Instruct")

client = OpenAI(base_url=base_url, api_key=api_key)

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a concise platform engineering assistant."},
        {"role": "user", "content": "ECS GPU에서 vLLM을 운영할 때 주의할 점을 3개만 알려줘."},
    ],
    temperature=0.2,
)

print(response.choices[0].message.content)
