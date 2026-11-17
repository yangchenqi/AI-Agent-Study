import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_api_key: str
    openai_base_url: str | None = None
    model_name: str
    database_url: str
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    openai_base_url: str | None = "https://api.deepseek.com"
    model_name: str = "deepseek-flash"
    database_url: str = ""

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')