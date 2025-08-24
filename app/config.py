from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    TELEGRAM_TOKEN: str = os.getenv("TELEGRAM_TOKEN")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    API_URL: str = os.getenv("API_URL")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:password@db:5432/astrodb")

settings = Settings()