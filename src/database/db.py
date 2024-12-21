import contextlib

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)

from src.conf.config import settings

class DatabaseSessionManager:
    def __init__(self, url: str):
        """AI is creating summary for __init__

        Args:
            url (str): [description]
        """
        self._engine: AsyncEngine | None = create_async_engine(url)
        self._session_maker: async_sessionmaker = async_sessionmaker(
            autoflush=False, autocommit=False, bind=self._engine
        )

    @contextlib.asynccontextmanager
    async def session(self):
        """AI is creating summary for session

        Raises:
            Exception: [description]

        Yields:
            [type]: [description]
        """
        if self._session_maker is None:
            raise Exception("Database session is not initialized")
        session = self._session_maker()
        try:
            yield session
        except SQLAlchemyError as e:
            await session.rollback()
            raise  # Re-raise the original error
        finally:
            await session.close()

sessionmanager = DatabaseSessionManager(settings.database_url)

async def get_db():
    """AI is creating summary for get_db

    Yields:
        [type]: [description]
    """
    async with sessionmanager.session() as session:
        yield session
