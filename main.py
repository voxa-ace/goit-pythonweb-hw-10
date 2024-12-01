from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from src.api.contacts import router as contact_router
from src.api.birthdays import router as birthday_router
from src.database.db import get_db

app = FastAPI()

# Include routers for contacts and birthdays
app.include_router(contact_router, prefix="/contacts", tags=["Contacts"])
app.include_router(birthday_router, prefix="/birthdays", tags=["Birthdays"])

# Add a root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Contacts API!",
        "docs": "/docs",
        "redoc": "/redoc",
    }

# Add a database health check endpoint
@app.get("/db-check")
def check_database_connection(db: Session = Depends(get_db)):
    """
    Endpoint to check database connection.
    """
    try:
        # Execute a simple query to verify the database connection
        result = db.execute("SELECT 1").fetchone()
        if result:
            return {"status": "success", "message": "Database connection is OK"}
        else:
            raise HTTPException(status_code=500, detail="Database connection test failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")
