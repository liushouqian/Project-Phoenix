from openai import OpenAI

from app.core.config import settings
from app.core.prompts import SYSTEM_PROMPT

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.OPENAI_BASE_URL,
)


def _call_model(model_name: str, message: str) -> str:
    print(f"[DEBUG] Trying model: {model_name}")

    response = client.chat.completions.create(
        model=model_name,
        temperature=settings.OPENAI_TEMPERATURE,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    content = response.choices[0].message.content or ""
    print(f"[DEBUG] Model success: {model_name}")
    return content


def generate_reply(message: str) -> str:
    if not message.strip():
        return "Message cannot be empty."

    primary_model = settings.OPENAI_MODEL
    fallback_model = settings.OPENAI_FALLBACK_MODEL
    print(f"[DEBUG] Primary model from settings: {primary_model}")
    print(f"[DEBUG] Fallback model from settings: {fallback_model}")

    try:
        return _call_model(primary_model, message)
    except Exception as primary_error:
        print(f"[WARN] Primary model failed: {primary_model}")
        print(f"[WARN] Primary error: {primary_error}")

        if fallback_model:
            try:
                return _call_model(fallback_model, message)
            except Exception as fallback_error:
                print(f"[WARN] Fallback model failed: {fallback_model}")
                print(f"[WARN] Fallback error: {fallback_error}")
                return (
                    "LLM request failed.\n"
                    f"Primary model ({primary_model}): {primary_error}\n"
                    f"Fallback model ({fallback_model}): {fallback_error}"
                )

        return f"LLM request failed: {primary_error}"