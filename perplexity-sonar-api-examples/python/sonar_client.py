from __future__ import annotations

import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DEFAULT_BASE_URL = "https://api.perplexity.ai"
DEFAULT_MODEL = "sonar-pro"


class SonarConfigError(RuntimeError):
    """Raised when local configuration is missing or unsafe."""


def get_api_key() -> str:
    api_key = os.getenv("PERPLEXITY_API_KEY", "")
    if not api_key or api_key == "pplx-your-api-key":
        raise SonarConfigError(
            "Set PERPLEXITY_API_KEY in your .env file before running this example."
        )
    return api_key


def get_client() -> OpenAI:
    return OpenAI(
        api_key=get_api_key(),
        base_url=os.getenv("PERPLEXITY_BASE_URL", DEFAULT_BASE_URL),
    )


def get_model() -> str:
    return os.getenv("PERPLEXITY_MODEL", DEFAULT_MODEL)


def create_completion(
    messages: list[dict[str, str]],
    *,
    model: str | None = None,
    stream: bool = False,
    extra_body: dict[str, Any] | None = None,
):
    """Create a Sonar chat completion through the OpenAI-compatible SDK."""
    client = get_client()
    return client.chat.completions.create(
        model=model or get_model(),
        messages=messages,
        stream=stream,
        extra_body=extra_body,
    )
