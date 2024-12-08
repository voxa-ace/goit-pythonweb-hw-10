import cloudinary
import cloudinary.uploader
from fastapi import HTTPException
from src.conf.config import settings  # Import settings

# Configure Cloudinary using the environment variable
cloudinary.config(
    cloudinary_url=settings.cloudinary_url  # Dynamic configuration from .env
)

def upload_avatar(file):
    """
    Uploads a user avatar to Cloudinary.

    Args:
        file: The file to be uploaded.

    Returns:
        str: URL of the uploaded avatar.

    Raises:
        HTTPException: If the upload fails.
    """
    try:
        # Upload the file to the "avatars" folder in Cloudinary
        result = cloudinary.uploader.upload(file, folder="avatars")
        return result.get("secure_url")  # Return the secure URL of the uploaded file
    except Exception as e:
        # Handle any exceptions during the upload process
        raise HTTPException(status_code=500, detail=f"Avatar upload failed: {str(e)}")
