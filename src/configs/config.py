import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str = os.environ.get("APP_BOT_TOKEN", "")
    BOT_TOKEN2: str = os.environ.get("APP_BOT_TOKEN", "2")
    TIME_OUT: int = os.environ.get("APP_TIMEOUT", 100)


settings = Settings()
