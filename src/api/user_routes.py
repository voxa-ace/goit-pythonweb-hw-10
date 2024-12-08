
from fastapi import APIRouter, Depends, UploadFile, HTTPException
from sqlalchemy.orm import Session
from src.auth import get_current_user
from src.utils import upload_avatar
from src.database.db import get_db
from src.services.user_service import update_user_avatar, verify_email
from src.schemas import UserResponse

router = APIRouter()

@router.post("/avatar", response_model=UserResponse)
async def update_avatar(
    file: UploadFile,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")
    avatar_url = upload_avatar(file.file)
    return update_user_avatar(db, current_user.id, avatar_url)

@router.get("/verify-email/{token}", response_model=dict)
async def verify_user_email(
    token: str,
    db: Session = Depends(get_db)
):
    success = verify_email(db, token)
    if success:
        return {"message": "Email verified successfully."}
    raise HTTPException(status_code=400, detail="Invalid or expired verification token.")
