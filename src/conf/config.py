from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str  # Database URL
    secret_key: str  # Secret key for JWT
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 15

    class Config:
        env_file = ".env"

settings = Settings()
