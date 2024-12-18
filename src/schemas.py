from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class UserLogin(BaseModel):
    email: str
    password: str

# Схема користувача
class User(BaseModel):
    id: int
    username: str
    email: str
    avatar: str


# Схема для запиту реєстрації
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Схема для токену
class Token(BaseModel):
    access_token: str
    token_type: str
    class Config:
        from_attributes = True

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone_number: str
    birth_date: date
    additional_info: Optional[str]

class ContactCreate(ContactBase):
    pass

class ContactResponse(BaseModel):
    id: int

    class Config:
        from_attributes = True

class ContactFullResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date  : date
    additional_info: str
