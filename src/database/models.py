from sqlalchemy import Column, Integer, String, Date, DateTime, Boolean, func, \
ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase

class Base(DeclarativeBase):
    """AI is creating summary for Base

    Args:
        DeclarativeBase ([type]): [description]
    """
    pass

class Contact(Base):
    """AI is creating summary for Contact

    Args:
        Base ([type]): [description]
    """
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100), index=True)
    email = Column(String(150), unique=True, index=True)
    phone_number = Column(String(15), unique=True)
    birth_date = Column(Date)
    additional_info = Column(String, nullable=True)
    user_id = Column(
        "user_id", ForeignKey("users.id", ondelete="CASCADE"), default=None
    )
    user = relationship("User", backref="contacts")

class User(Base):
    """AI is creating summary for User

    Args:
        Base ([type]): [description]
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=func.now())
    avatar = Column(String(255), nullable=True)
    confirmed = Column(Boolean, default=False)

