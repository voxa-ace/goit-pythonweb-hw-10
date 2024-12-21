from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.services.auth import get_current_user
from src.services.contact_service import (
    get_all_contacts,
    create_new_contact,
    update_existing_contact,
    delete_existing_contact,
    get_existing_contact,
)
from src.schemas import ContactCreate, ContactResponse, User, ContactFullResponse
from src.database.db import get_db

# Create router
router = APIRouter(prefix="/contacts")


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(
    contact: ContactCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """AI is creating summary for create_contact

    Args:
        contact (ContactCreate): [description]
        db (AsyncSession, optional): [description]. Defaults to Depends(get_db).
        current_user (User, optional): [description]. Defaults to Depends(get_current_user).

    Raises:
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    print(contact)
    print(current_user)
    contact_id = await create_new_contact(db, contact, current_user)
    if contact_id == None:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="contact already exists")
    print(contact_id)
    return {"id":contact_id}


@router.get("/", response_model=list[ContactResponse])
async def get_contacts(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """AI is creating summary for get_contacts

    Args:
        skip (int, optional): [description]. Defaults to 0.
        limit (int, optional): [description]. Defaults to 100.
        db (AsyncSession, optional): [description]. Defaults to Depends(get_db).
        current_user (User, optional): [description]. Defaults to Depends(get_current_user).

    Returns:
        [type]: [description]
    """
    contacts = await get_all_contacts(db, skip, limit, current_user)
    return contacts

@router.get("/{contact_id}", response_model=ContactFullResponse)
async def get_contact(
    contact_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """AI is creating summary for get_contact

    Args:
        contact_id (int): [description]
        db (AsyncSession, optional): [description]. Defaults to Depends(get_db).
        current_user (User, optional): [description]. Defaults to Depends(get_current_user).

    Raises:
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    contact = await get_existing_contact(db, contact_id, current_user)
    if not contact:
        raise HTTPException(detail="Contact not found or not accessible by this user.",
        status_code=status.HTTP_404_NOT_FOUND)
    return {"id": contact.id,
            "first_name": contact.first_name,
            "last_name": contact.last_name,
            "email": contact.email,
            "phone_number": contact.phone_number,
            "birth_date": contact.birth_date,
            "additional_info": contact.additional_info,
            }

@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(
    contact_id: int,
    contact: ContactCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """AI is creating summary for update_contact

    Args:
        contact_id (int): [description]
        contact (ContactCreate): [description]
        db (AsyncSession, optional): [description]. Defaults to Depends(get_db).
        current_user (User, optional): [description]. Defaults to Depends(get_current_user).

    Raises:
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    result = await update_existing_contact(db, contact_id, contact, current_user)
    if result == None:
        raise HTTPException(detail="Contact not found or not accessible by this user.", 
        status_code=status.HTTP_404_NOT_FOUND)
    return result

@router.delete("/{contact_id}", response_model=dict)
async def delete_contact(
    contact_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """AI is creating summary for delete_contact

    Args:
        contact_id (int): [description]
        db (AsyncSession, optional): [description]. Defaults to Depends(get_db).
        current_user (User, optional): [description]. Defaults to Depends(get_current_user).

    Raises:
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    result = await delete_existing_contact(db, contact_id, current_user)
    if result == None:
        raise HTTPException(detail="Contact not found or not accessible by this user.",
        status_code=status.HTTP_404_NOT_FOUND)
    return result
