from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class UserLogin(BaseModel):
    """def __init__(self, url: str):
        self._engine: AsyncEngine | None = create_async_engine(url)
        self._session_maker: async_sessionmaker = async_sessionmaker(
            autoflush=False, autocommit=False, bind=self._engine
        )"""
    email: str
    password: str

# Схема користувача
class User(BaseModel):
    """AI is creating summary for User

    Args:
        BaseModel ([type]): [description]
    """
    id: int
    username: str
    email: str
    avatar: str


# Схема для запиту реєстрації
class UserCreate(BaseModel):
    """AI is creating summary for UserCreate

    Args:
        BaseModel ([type]): [description]
    """
    username: str
    email: str
    password: str

# Схема для токену
class Token(BaseModel):
    """AI is creating summary for Token

    Args:
        BaseModel ([type]): [description]
    """
    access_token: str
    token_type: str
    class Config:
        from_attributes = True

class ContactBase(BaseModel):
    """AI is creating summary for ContactBase

    Args:
        BaseModel ([type]): [description]
    """
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birth_date: date
    additional_info: Optional[str]

class ContactCreate(ContactBase):
    """AI is creating summary for ContactCreate

    Args:
        ContactBase ([type]): [description]
    """
    pass

class ContactResponse(BaseModel):
    """AI is creating summary for ContactResponse

    Args:
        BaseModel ([type]): [description]
    """
    id: int

    class Config:
        from_attributes = True

class ContactFullResponse(BaseModel):
    """AI is creating summary for ContactFullResponse

    Args:
        BaseModel ([type]): [description]
    """
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date  : date
    additional_info: str
