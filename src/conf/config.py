from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    cloudinary_url: str  
    jwt_secret: str
    jwt_algorithm: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

print("Settings initialized:", Settings.dict())
