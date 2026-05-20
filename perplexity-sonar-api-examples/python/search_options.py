from __future__ import annotations

from sonar_client import create_completion

messages = [
    {
        "role": "system",
        "content": "You are a technical research assistant. Answer in Korean.",
    },
    {
        "role": "user",
        "content": "Find recent information about Perplexity Sonar API for developers.",
    },
]

# Perplexity-specific options can be passed through extra_body when using the OpenAI SDK.
# Verify current options in the official docs before production use.
completion = create_completion(
    messages,
    extra_body={
        "search_mode": "web",
        "search_recency_filter": "month",
        "return_related_questions": True,
    },
)

print(completion.choices[0].message.content)

related_questions = getattr(completion, "related_questions", None)
if related_questions:
    print("\nRELATED QUESTIONS")
    for question in related_questions:
        print(f"- {question}")
