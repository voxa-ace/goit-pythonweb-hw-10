from sqlalchemy.orm import Session
from src.database.models import User
from src.schemas import UserCreate

def get_user_by_email(db: Session, email: str):
    """
    Retrieve a user by email.
    """
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    """
    Create a new user in the database.
    """
    new_user = User(
        email=user.email,
        hashed_password=user.hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
