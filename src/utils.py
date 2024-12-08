
import cloudinary
import cloudinary.uploader
from fastapi import HTTPException

# Configure Cloudinary
cloudinary.config(
    cloud_name="your_cloud_name",
    api_key="your_api_key",
    api_secret="your_api_secret"
)

def upload_avatar(file):
    try:
        result = cloudinary.uploader.upload(file, folder="avatars")
        return result.get("secure_url")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Avatar upload failed: {str(e)}")
