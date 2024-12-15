from fastapi import FastAPI
import uvicorn
from src.api import auth, users, contacts

app = FastAPI()

app.include_router(contacts.router, prefix="/api")
# app.include_router(birthdays.router, prefix="/api")
app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
