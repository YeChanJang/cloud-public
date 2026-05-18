from typing import Literal
from pydantic import BaseModel
from ollama import chat


class SupportTicket(BaseModel):
    category: Literal["billing", "technical", "account", "other"]
    priority: Literal["low", "medium", "high"]
    summary: str


response = chat(
    model="gemma3",
    messages=[
        {
            "role": "user",
            "content": "I was charged twice this month and need a refund as soon as possible.",
        }
    ],
    format=SupportTicket.model_json_schema(),
    options={"temperature": 0},
)

ticket = SupportTicket.model_validate_json(response.message.content)
print(ticket)
