from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.contacts import router as contact_router
from src.api.birthdays import router as birthday_router
from src.api.auth import router as auth_router
from src.database.db import Base, engine

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(contact_router, prefix="/contacts", tags=["Contacts"])
app.include_router(birthday_router, prefix="/birthdays", tags=["Birthdays"])

# Root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Contacts API!",
        "docs": "/docs",
        "redoc": "/redoc",
    }
