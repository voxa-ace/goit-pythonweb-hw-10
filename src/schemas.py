
from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: int
    email: EmailStr
    is_verified: bool

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    avatar: Optional[str]

    class Config:
        orm_mode = True

class ContactBase(BaseModel):
    name: str
    phone: str

class ContactCreate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
