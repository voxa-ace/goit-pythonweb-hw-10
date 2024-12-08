
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.contacts import router as contact_router
from src.api.birthdays import router as birthday_router
from src.auth import auth_router

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust for specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(contact_router, prefix="/contacts", tags=["Contacts"])
app.include_router(birthday_router, prefix="/birthdays", tags=["Birthdays"])
app.include_router(auth_router, tags=["Auth"])

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Contacts API!",
        "docs": "/docs",
        "redoc": "/redoc",
    }
