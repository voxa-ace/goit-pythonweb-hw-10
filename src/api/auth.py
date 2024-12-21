from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from src.schemas import UserCreate, Token, User, UserLogin
from src.services.auth import create_access_token, Hash
from src.services.user_service import UserService
from src.database.db import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

# Реєстрація користувача
@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
async def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    """AI is creating summary for register_user

    Args:
        user_data (UserCreate): [description]
        db (Session, optional): [description]. Defaults to Depends(get_db).

    Raises:
        HTTPException: [description]
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    user_service = UserService(db)

    email_user = await user_service.get_user_by_email(user_data.email)
    if email_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Користувач з таким email вже існує",
        )

    username_user = await user_service.get_user_by_username(user_data.username)
    if username_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Користувач з таким іменем вже існує",
        )
    user_data.password = Hash().get_password_hash(user_data.password)
    new_user = await user_service.create_user(user_data)

    return new_user

# Логін користувача
@router.post("/login", response_model=Token)
async def login_user(
    form_data: UserLogin, db: Session = Depends(get_db)
):
    """AI is creating summary for login_user

    Args:
        form_data (UserLogin): [description]
        db (Session, optional): [description]. Defaults to Depends(get_db).

    Raises:
        HTTPException: [description]

    Returns:
        [type]: [description]
    """
    user_service = UserService(db)
    user = await user_service.get_user_by_email(form_data.email)
    print(user)
    if not user or not Hash().verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неправильний логін або пароль",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = await create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
