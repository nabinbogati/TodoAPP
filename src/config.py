from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # secrets
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # database
    SQLITE_PATH: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )


settings = Settings()
