import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
  OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
  OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "")
  OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "google/gemma-4-26b-a4b-it:free")
  OPENAI_FALLBACK_MODEL: str = os.getenv("OPENAI_FALLBACK_MODEL", "")
  OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", 0.7))
  OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", 1000))
  OPENAI_TOP_P: float = float(os.getenv("OPENAI_TOP_P", 1))
  OPENAI_PRESENCE_PENALTY: float = float(os.getenv("OPENAI_PRESENCE_PENALTY", 0))
  OPENAI_FREQUENCY_PENALTY: float = float(os.getenv("OPENAI_FREQUENCY_PENALTY", 0))


settings = Settings()