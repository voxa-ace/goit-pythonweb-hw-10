from sqlalchemy import Column, Integer, String, Date
from src.database.db import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100), index=True)
    email = Column(String(150), unique=True, index=True)
    phone_number = Column(String(15), unique=True)
    birth_date = Column(Date)
    additional_info = Column(String, nullable=True)
