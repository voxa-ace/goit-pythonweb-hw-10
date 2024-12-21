from fastapi import APIRouter, Depends
from src.schemas import User
from src.services.auth import get_current_user

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=User)
async def me(user: User = Depends(get_current_user)):
    """AI is creating summary for me

    Args:
        user (User, optional): [description]. Defaults to Depends(get_current_user).

    Returns:
        [type]: [description]
    """
    return user
