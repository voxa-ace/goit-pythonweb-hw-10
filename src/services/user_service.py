from sqlalchemy.ext.asyncio import AsyncSession
from libgravatar import Gravatar

from src.repository.users import UserRepository
from src.schemas import UserCreate

class UserService:
    """AI is creating summary for 
    """
    def __init__(self, db: AsyncSession):
        """AI is creating summary for __init__

        Args:
            db (AsyncSession): [description]
        """
        self.repository = UserRepository(db)

    async def create_user(self, body: UserCreate):
        """AI is creating summary for create_user

        Args:
            body (UserCreate): [description]

        Returns:
            [type]: [description]
        """
        avatar = None
        try:
            g = Gravatar(body.email)
            avatar = g.get_image()
        except Exception as e:
            print(e)

        return await self.repository.create_user(body, avatar)

    async def get_user_by_id(self, user_id: int):
        """AI is creating summary for get_user_by_id

        Args:
            user_id (int): [description]

        Returns:
            [type]: [description]
        """
        return await self.repository.get_user_by_id(user_id)

    async def get_user_by_username(self, username: str):
        """AI is creating summary for get_user_by_username

        Args:
            username (str): [description]

        Returns:
            [type]: [description]
        """
        return await self.repository.get_user_by_username(username)

    async def get_user_by_email(self, email: str):
        """AI is creating summary for get_user_by_email

        Args:
            email (str): [description]

        Returns:
            [type]: [description]
        """
        return await self.repository.get_user_by_email(email)

