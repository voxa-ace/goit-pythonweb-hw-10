from sqlalchemy import Column, Integer, String, Boolean, Date
from src.database.db import Base

class User(Base):
    """
    User model for storing user authentication data.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)

class Contact(Base):
    """
    Contact model for storing contact details.
    """
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100), index=True)
    email = Column(String(150), unique=True, index=True)
    phone_number = Column(String(15), unique=True)
    birth_date = Column(Date)
    additional_info = Column(String, nullable=True)
    user_id = Column(Integer, index=True)  # Foreign Key for user
