from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import User
from src.schemas import UserCreate

class UserRepository:
    """AI is creating summary for 
    """
    def __init__(self, session: AsyncSession):
        """AI is creating summary for __init__

        Args:
            session (AsyncSession): [description]
        """
        self.db = session

    async def get_user_by_id(self, user_id: int) -> User | None:
        """AI is creating summary for get_user_by_id

        Returns:
            [type]: [description]
        """
        stmt = select(User).filter_by(id=user_id)
        user = await self.db.execute(stmt)
        return user.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> User | None:
        """AI is creating summary for get_user_by_username

        Returns:
            [type]: [description]
        """
        stmt = select(User).filter_by(username=username)
        user = await self.db.execute(stmt)
        return user.scalar_one_or_none()

    async def get_user_by_email(self, email: str) -> User | None:
        """AI is creating summary for get_user_by_email

        Returns:
            [type]: [description]
        """
        stmt = select(User).filter_by(email=email)
        user = await self.db.execute(stmt)
        return user.scalar_one_or_none()

    async def create_user(self, body: UserCreate, avatar: str = None) -> User:
        """AI is creating summary for create_user

        Args:
            body (UserCreate): [description]
            avatar (str, optional): [description]. Defaults to None.

        Returns:
            User: [description]
        """
        user = User(
            **body.model_dump(exclude_unset=True, exclude={"password"}),
            hashed_password=body.password,
            avatar=avatar
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user
