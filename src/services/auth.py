from datetime import datetime, timedelta, UTC
from typing import Optional

from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from src.database.db import get_db
from src.conf.config import settings
from src.services.user_service import UserService

class Hash:
    """AI is creating summary for 

    Returns:
        [type]: [description]
    """
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        """AI is creating summary for verify_password

        Args:
            plain_password ([type]): [description]
            hashed_password (bool): [description]

        Returns:
            [type]: [description]
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str):
        """AI is creating summary for get_password_hash

        Args:
            password (str): [description]

        Returns:
            [type]: [description]
        """
        return self.pwd_context.hash(password)

oauth2_scheme = HTTPBearer()

# define a function to generate a new access token
async def create_access_token(data: dict, expires_delta: Optional[int] = None):
    """AI is creating summary for create_access_token

    Args:
        data (dict): [description]
        expires_delta (Optional[int], optional): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + timedelta(seconds=expires_delta)
    else:
        expire = datetime.now(UTC) + timedelta(minutes=settings.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.jwt_secret, algorithm=settings.jwt_algorithm
    )
    return encoded_jwt

async def get_current_user(
    token: HTTPAuthorizationCredentials = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    """AI is creating summary for get_current_user

    Args:
        token (HTTPAuthorizationCredentials, optional): [description]. Defaults to Depends(oauth2_scheme).
        db (Session, optional): [description]. Defaults to Depends(get_db).

    Raises:
        credentials_exception: [description]
        credentials_exception: [description]
        credentials_exception: [description]

    Returns:
        [type]: [description]
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decode JWT
        token = token.credentials
        payload = jwt.decode(
            token, settings.jwt_secret, algorithms=[settings.jwt_algorithm]
        )
        username = payload["sub"]
        if username is None:
            raise credentials_exception
    except JWTError as e:
        raise credentials_exception
    user_service = UserService(db)
    user = await user_service.get_user_by_username(username)
    if user is None:
        raise credentials_exception
    return user

