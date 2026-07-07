import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
  OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
  OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "")
  OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "google/gemma-4-26b-a4b-it:free")
  OPENAI_FALLBACK_MODEL: str = os.getenv("OPENAI_FALLBACK_MODEL", "")
  OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", 0.7))


settings = Settings()