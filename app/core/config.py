from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', case_sensitive=False)
    app_name: str = "Pharmacy Inventory API"
    app_version: str = "0.1.0"
    app_description: str = "Backend API for pharmacy inventory management."
    debug: bool = True
    database_url: str


settings = Settings()
