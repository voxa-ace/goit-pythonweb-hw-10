from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.repository.contact_repository import (
    get_all_contacts_from_db,
    create_contact_in_db,
    update_contact_in_db,
    delete_contact_from_db,
    get_contact_by_id,
)

def get_all_contacts(db: Session, skip: int, limit: int):
    """Retrieve all contacts with pagination"""
    return get_all_contacts_from_db(db, skip, limit)

def create_new_contact(db: Session, contact_data):
    """Create a new contact in the database"""
    return create_contact_in_db(db, contact_data)

def update_existing_contact(db: Session, contact_id: int, updated_data):
    """Update an existing contact in the database"""
    return update_contact_in_db(db, contact_id, updated_data)

def delete_existing_contact(db: Session, contact_id: int):
    """Delete a contact from the database"""
    return delete_contact_from_db(db, contact_id)

def get_existing_contact(db: Session, contact_id: int):
    """Retrieve a contact by ID"""
    contact = get_contact_by_id(db, contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact
