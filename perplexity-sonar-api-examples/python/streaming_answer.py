from __future__ import annotations

from sonar_client import create_completion

messages = [
    {
        "role": "system",
        "content": "Answer in Korean with short paragraphs.",
    },
    {
        "role": "user",
        "content": "Explain Perplexity Sonar API as a developer blog example.",
    },
]

stream = create_completion(messages, stream=True)

for chunk in stream:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)

print()
