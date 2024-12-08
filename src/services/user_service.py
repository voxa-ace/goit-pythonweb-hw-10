
from sqlalchemy.orm import Session
from src.database.models import User
from fastapi import HTTPException

def update_user_avatar(db: Session, user_id: int, avatar_url: str):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    user.avatar = avatar_url
    db.commit()
    db.refresh(user)
    return user

def verify_email(db: Session, token: str):
    # Example of email verification logic
    user = db.query(User).filter(User.email_verification_token == token).first()
    if not user or user.is_verified:
        return False
    user.is_verified = True
    user.email_verification_token = None  # Clear the token
    db.commit()
    return True
