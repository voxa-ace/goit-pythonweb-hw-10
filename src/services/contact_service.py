
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.repository.contact_repository import (
    get_all_contacts_from_db,
    create_contact_in_db,
    update_contact_in_db,
    delete_contact_from_db,
    get_contact_by_id_and_user,
)

def get_all_contacts(db: Session, skip: int, limit: int, user_id: int):
    return get_all_contacts_from_db(db, skip, limit, user_id)

def create_new_contact(db: Session, contact_data, user_id: int):
    contact_data.user_id = user_id
    return create_contact_in_db(db, contact_data)

def update_existing_contact(db: Session, contact_id: int, updated_data, user_id: int):
    contact = get_contact_by_id_and_user(db, contact_id, user_id)
    if not contact:
        raise NoResultFound("Contact not found or not accessible by this user.")
    return update_contact_in_db(db, contact_id, updated_data)

def delete_existing_contact(db: Session, contact_id: int, user_id: int):
    contact = get_contact_by_id_and_user(db, contact_id, user_id)
    if not contact:
        raise NoResultFound("Contact not found or not accessible by this user.")
    delete_contact_from_db(db, contact_id)
    return {"message": "Contact deleted successfully."}

def get_existing_contact(db: Session, contact_id: int, user_id: int):
    contact = get_contact_by_id_and_user(db, contact_id, user_id)
    if not contact:
        raise NoResultFound("Contact not found or not accessible by this user.")
    return contact
