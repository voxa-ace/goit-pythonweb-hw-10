from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from fastapi import Depends

@app.on_event("startup")
async def startup():
    """
    Initialize the rate limiter.
    """
    redis_url = "redis://localhost:6379"  # Replace with your Redis URL
    await FastAPILimiter.init(redis_url)

@router.get("/me", dependencies=[Depends(RateLimiter(times=5, seconds=60))])
def get_user_profile():
    """
    Get the profile of the authenticated user (limited to 5 requests per minute).
    """
    return {"message": "User profile data"}
