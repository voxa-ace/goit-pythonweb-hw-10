from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    cloudinary_url: str
    jwt_secret: str
    jwt_algorithm: str
    access_token_expire_minutes: int = 30
    token_url: str  # Endpoint for obtaining tokens

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
print(settings)