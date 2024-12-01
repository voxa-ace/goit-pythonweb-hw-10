from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas import UserCreate, TokenResponse
from src.services.auth_service import authenticate_user, create_access_token, hash_password
from src.repository.user_repository import create_user
from src.database.db import get_db

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.
    """
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=409, detail="Email already exists")
    user.hashed_password = hash_password(user.password)
    return create_user(db, user)

@router.post("/login", response_model=TokenResponse)
def login(user: UserCreate, db: Session = Depends(get_db)):
    """
    Login a user and return an access token.
    """
    authenticated_user = authenticate_user(db, user.email, user.password)
    return {"access_token": create_access_token({"sub": authenticated_user.email})}
