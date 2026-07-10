from openai import OpenAI

from app.core.config import settings
from app.core.prompts import SYSTEM_PROMPT
from app.services.conversation_store import get_history, append_message

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.OPENAI_BASE_URL,
)


def _call_model(model_name: str, message: str, history: list[dict[str, str]]) -> str:
    print(f"[DEBUG] Trying model: {model_name}")

    response = client.chat.completions.create(
        model=model_name,
        temperature=settings.OPENAI_TEMPERATURE,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            *history,
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    content = response.choices[0].message.content or ""
    print(f"[DEBUG] Model success: {model_name}")
    return content


def generate_reply(session_id: str, message: str) -> str:
    if not message.strip():
        return "Message cannot be empty."

    history = get_history(session_id)
    primary_model = settings.OPENAI_MODEL
    fallback_model = settings.OPENAI_FALLBACK_MODEL

    print("[DEBUG] incoming session_id:", session_id)
    print("[DEBUG] incoming message:", message)
    print("[DEBUG] history before:", history)

    try:
        reply = _call_model(primary_model, message, history)
        append_message(session_id, "user", message)
        append_message(session_id, "assistant", reply)

        print("[DEBUG] history after:", get_history(session_id))

        return reply
    except Exception as primary_error:
        print(f"[WARN] Primary model failed: {primary_model}")
        print(f"[WARN] Primary error: {primary_error}")

        if fallback_model:
            try:
                reply = _call_model(fallback_model, message, history)
                append_message(session_id, "user", message)
                append_message(session_id, "assistant", reply)

                print("[DEBUG] history after:", get_history(session_id))
                return reply
            except Exception as fallback_error:
                print(f"[WARN] Fallback model failed: {fallback_model}")
                print(f"[WARN] Fallback error: {fallback_error}")
                return (
                    "LLM request failed.\n"
                    f"Primary model ({primary_model}): {primary_error}\n"
                    f"Fallback model ({fallback_model}): {fallback_error}"
                )

        return f"LLM request failed: {primary_error}"