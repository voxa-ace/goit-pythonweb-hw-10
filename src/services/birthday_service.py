from sqlalchemy.orm import Session
from src.repository.birthday_repository import get_contacts_with_upcoming_birthdays

def get_upcoming_birthdays(db: Session, days: int):
    """Retrieve contacts with upcoming birthdays within the specified range"""
    return get_contacts_with_upcoming_birthdays(db, days)
