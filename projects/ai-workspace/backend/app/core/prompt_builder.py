from app.core.prompts import SYSTEM_PROMPT

def build_messages(
  history: list[dict[str, str]],
  user_message: str,
) -> list[dict[str, str]]:
  return [
    {
        "role": "system",
        "content": SYSTEM_PROMPT,
    },
    *history,
    {
        "role": "user",
        "content": user_message,
    },
  ]