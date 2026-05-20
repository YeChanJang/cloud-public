from __future__ import annotations

from sonar_client import create_completion

messages = [
    {
        "role": "system",
        "content": "Answer in Korean. Explain with source-aware reasoning.",
    },
    {
        "role": "user",
        "content": "Summarize recent AI API trends for developers in 2026.",
    },
]

completion = create_completion(messages)

print("ANSWER")
print(completion.choices[0].message.content)

print("\nCITATIONS")
for idx, citation in enumerate(getattr(completion, "citations", []) or [], start=1):
    print(f"[{idx}] {citation}")

print("\nSEARCH RESULTS")
for idx, result in enumerate(getattr(completion, "search_results", []) or [], start=1):
    title = result.get("title", "") if isinstance(result, dict) else getattr(result, "title", "")
    url = result.get("url", "") if isinstance(result, dict) else getattr(result, "url", "")
    print(f"[{idx}] {title} - {url}")

print("\nUSAGE")
print(completion.usage)
