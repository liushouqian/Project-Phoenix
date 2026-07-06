from openai import OpenAI

from app.core.config import settings

client = OpenAI(
  api_key=settings.OPENAI_API_KEY,
  base_url=settings.OPENAI_BASE_URL,
)


def generate_reply(message: str) -> str:
  response = client.chat.completions.create(
    model=settings.OPENAI_MODEL,
    messages=[
      {
        "role": "system",
        "content": "You are a helpful AI assistant for Project Phoenix.",
      },
      {
        "role": "user",
        "content": message,
      },
    ],
  )

  return response.choices[0].message.content or ""