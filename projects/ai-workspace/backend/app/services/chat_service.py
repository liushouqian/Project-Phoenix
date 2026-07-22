from openai import OpenAI

from app.core.config import settings
from app.services.conversation_manager import get_recent_history, append_message
from app.core.prompt_builder import build_messages
from app.core.exceptions import LLMServiceError

client = OpenAI(
    api_key=settings.OPENAI_API_KEY,
    base_url=settings.OPENAI_BASE_URL,
)


def _call_model(model_name: str, message: str, history: list[dict[str, str]]) -> str:
    print(f"[DEBUG] Trying model: {model_name}")

    messages = build_messages(
      history,
      message,
    )

    response = client.chat.completions.create(
        model=model_name,
        temperature=settings.OPENAI_TEMPERATURE,
        max_tokens=settings.OPENAI_MAX_TOKENS,
        top_p=settings.OPENAI_TOP_P,
        presence_penalty=settings.OPENAI_PRESENCE_PENALTY,
        frequency_penalty=settings.OPENAI_FREQUENCY_PENALTY,
        messages=messages,
    )

    content = response.choices[0].message.content or ""
    print(f"[DEBUG] Model success: {model_name}")
    print(f"[DEBUG] temperature: {settings.OPENAI_TEMPERATURE}")
    print(f"[DEBUG] max_tokens: {settings.OPENAI_MAX_TOKENS}")
    print(f"[DEBUG] top_p: {settings.OPENAI_TOP_P}")
    return content


def generate_reply(session_id: str, message: str) -> str:
    if not message.strip():
        return "Message cannot be empty."

    history = get_recent_history(session_id, limit=10)
    primary_model = settings.OPENAI_MODEL
    fallback_model = settings.OPENAI_FALLBACK_MODEL

    print("[DEBUG] incoming session_id:", session_id)
    print("[DEBUG] incoming message:", message)
    print("[DEBUG] history before:", history)

    try:
        reply = _call_model(primary_model, message, history)
        append_message(session_id, "user", message)
        append_message(session_id, "assistant", reply)

        print("[DEBUG] history after:", get_recent_history(session_id))

        return reply
    except Exception as primary_error:
        print(f"[WARN] Primary model failed: {primary_model}")
        print(f"[WARN] Primary error: {primary_error}")

        if fallback_model:
            try:
                reply = _call_model(fallback_model, message, history)
                append_message(session_id, "user", message)
                append_message(session_id, "assistant", reply)

                print("[DEBUG] history after:", get_recent_history(session_id))
                return reply
            except Exception as fallback_error:
                print(f"[WARN] Fallback model failed: {fallback_model}")
                print(f"[WARN] Fallback error: {fallback_error}")
                raise LLMServiceError("LLM request failed")

        raise LLMServiceError("Primary model failed")