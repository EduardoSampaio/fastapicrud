from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    DATABASE_URL: str = os.environ.get('DATABASE_URL')
    JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY")
    JWT_REFRESH_SECRET_KEY: str = os.environ.get("JWT_REFRESH_SECRET_KEY")
    REFRESH_TOKEN_EXPIRES_IN: int = os.environ.get("REFRESH_TOKEN_EXPIRES_IN")
    ACCESS_TOKEN_EXPIRES_IN: int = os.environ.get("ACCESS_TOKEN_EXPIRES_IN")
    JWT_ALGORITHM: str = os.environ.get("JWT_ALGORITHM")
    GOOGLE_CLIENT_ID: str = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.environ.get("GOOGLE_CLIENT_SECRET")

    class Config:
        env_file = '../.env'
        env_file_encoding = "utf-8"


settings = Settings()
