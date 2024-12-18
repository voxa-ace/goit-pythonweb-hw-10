from src.database.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import NoResultFound
from src.repository.contact_repository import (
    get_all_contacts_from_db,
    create_contact_in_db,
    update_contact_in_db,
    delete_contact_from_db,
    get_contact_by_id_and_user,
)

async def get_all_contacts(db: AsyncSession, skip: int, limit: int, user: User):
    return await get_all_contacts_from_db(db, skip, limit, user)

async def create_new_contact(db: AsyncSession, contact_data, user: User):
    result = await create_contact_in_db(db, contact_data, user)
    return result

async def update_existing_contact(db: AsyncSession, contact_id: int, updated_data, user: User):
    contact = await get_contact_by_id_and_user(db, contact_id, user)
    if not contact:
        return None
    return await update_contact_in_db(db, contact_id, updated_data, user)

async def delete_existing_contact(db: AsyncSession, contact_id: int, user: User):
    contact = await get_contact_by_id_and_user(db, contact_id, user)
    if not contact:
        return None
    await delete_contact_from_db(db, contact_id, user)
    return {"message": "Contact deleted successfully."}

async def get_existing_contact(db: AsyncSession, contact_id: int, user: User):
    contact = await get_contact_by_id_and_user(db, contact_id, user)
    
    return contact
