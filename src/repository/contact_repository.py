
from sqlalchemy.orm import Session
from src.database.models import Contact

def get_all_contacts_from_db(db: Session, skip: int, limit: int, user_id: int):
    return db.query(Contact).filter(Contact.user_id == user_id).offset(skip).limit(limit).all()

def create_contact_in_db(db: Session, contact_data):
    new_contact = Contact(**contact_data.dict())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

def update_contact_in_db(db: Session, contact_id: int, updated_data):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        for key, value in updated_data.dict().items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
    return contact

def delete_contact_from_db(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()

def get_contact_by_id_and_user(db: Session, contact_id: int, user_id: int):
    return db.query(Contact).filter(Contact.id == contact_id, Contact.user_id == user_id).first()
