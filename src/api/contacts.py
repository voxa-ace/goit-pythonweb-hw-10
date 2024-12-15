from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.services.auth import get_current_user
from src.services.contact_service import (
    get_all_contacts,
    create_new_contact,
    update_existing_contact,
    delete_existing_contact,
    get_existing_contact,
)
from src.schemas import ContactCreate, ContactResponse, User
from src.database.db import get_db

# Create router
router = APIRouter()


@router.post("/", response_model=ContactResponse)
async def create_contact(
    contact: ContactCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    print(contact)
    print(current_user)
    contact_id = await create_new_contact(db, contact, current_user.id)
    print(contact_id)
    return {"id":contact_id, "user_id":current_user.id}


@router.get("/", response_model=list[ContactResponse])
def get_contacts(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_all_contacts(db, skip, limit, current_user.id)

@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact(
    contact_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_existing_contact(db, contact_id, current_user.id)

@router.put("/{contact_id}", response_model=ContactResponse)
def update_contact(
    contact_id: int,
    contact: ContactCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_existing_contact(db, contact_id, contact, current_user.id)

@router.delete("/{contact_id}", response_model=dict)
def delete_contact(
    contact_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_existing_contact(db, contact_id, current_user.id)
