from sqlalchemy.ext.asyncio import AsyncSession
from src.database.models import Contact, User
from sqlalchemy import select

async def get_all_contacts_from_db(db: AsyncSession, skip: int, limit: int, user: User):
    query = select(Contact).filter_by(user=user).offset(skip).limit(limit)
    result = await db.execute(query)
    contacts = result.scalars().all()
    return contacts

async def check_contact(db: AsyncSession, user: User, email: str, phone_number: str):
    query = select(Contact).filter_by(user=user).where((Contact.email==email) or (Contact.phone_number==phone_number))
    result = await db.execute(query)
    return result.scalars().first()

async def create_contact_in_db(db: AsyncSession, contact_data, user):
    is_exist = await check_contact(db=db, user=user, email=contact_data.email, phone_number=contact_data.phone_number)
    print(is_exist)
    if is_exist != None:
        return None
    new_contact = Contact(**contact_data.model_dump(exclude_unset=True), user=user)
    print(new_contact)
    db.add(new_contact)
    await db.commit()
    await db.refresh(new_contact)
    print(new_contact)
    contact_id = new_contact.id
    return contact_id

# async def create_tag(self, body: TagModel) -> Tag:
#     tag = Tag(**body.model_dump(exclude_unset=True))
#     self.db.add(tag)
#     await self.db.commit()
#     await self.db.refresh(tag)
#     return tag

async def update_contact_in_db(db: AsyncSession, contact_id: int, updated_data, user):
    query = select(Contact).filter_by(user=user).where(Contact.id == contact_id)
    result = await db.execute(query)
    contact = result.scalars().first()
    if contact:
        for key, value in updated_data.dict().items():
            setattr(contact, key, value)
        await db.commit()
        await db.refresh(contact)
    return contact

async def delete_contact_from_db(db: AsyncSession, contact_id: int, user: User):
    query = select(Contact).filter_by(user=user).where(Contact.id == contact_id)
    result = await db.execute(query)
    contact = result.scalars().first()    
    if contact:
        await db.delete(contact)
        await db.commit()

async def get_contact_by_id_and_user(db: AsyncSession, contact_id: int, user: User):
    query = select(Contact).filter_by(user=user).where(Contact.id == contact_id)
    result = await db.execute(query)
    contact = result.scalars().first()
    return contact
