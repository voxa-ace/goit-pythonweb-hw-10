from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from src.database.models import Contact

def get_contacts_with_upcoming_birthdays(db: Session, days: int = 7):
    """Retrieve contacts with upcoming birthdays within the specified range"""
    today = datetime.today().date()
    end_date = today + timedelta(days=days)
    return db.query(Contact).filter(
        Contact.birthday >= today,
        Contact.birthday <= end_date
    ).all()
