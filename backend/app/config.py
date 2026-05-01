import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")

    REDIS_HOST = os.getenv("REDIS_HOST")

    SHADOW_MODE = os.getenv("SHADOW_MODE", "true") == "true"
    RATE_LIMIT = int(os.getenv("RATE_LIMIT_PER_MIN", 60))


settings = Settings()