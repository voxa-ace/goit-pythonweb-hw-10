from sqlalchemy.orm import Session
from src.database.models import Contact

def get_all_contacts_from_db(db: Session, skip: int, limit: int):
    """Retrieve all contacts with pagination"""
    return db.query(Contact).offset(skip).limit(limit).all()

def create_contact_in_db(db: Session, contact_data):
    """Create a new contact"""
    new_contact = Contact(**contact_data.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

def update_contact_in_db(db: Session, contact_id: int, updated_data):
    """Update an existing contact"""
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        for key, value in updated_data.items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact

def delete_contact_from_db(db: Session, contact_id: int):
    """Delete a contact by ID"""
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

def get_contact_by_id(db: Session, contact_id: int):
    """Retrieve a contact by ID"""
    return db.query(Contact).filter(Contact.id == contact_id).first()
