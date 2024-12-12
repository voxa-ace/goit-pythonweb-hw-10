from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.auth import create_access_token, oauth2_scheme
from src.conf.config import settings

app = FastAPI()

# Приклад простої функції для аутентифікації користувача (потрібно реалізувати справжню логіку)
def authenticate_user(username: str, password: str):
    # Тут ви повинні перевірити користувача в базі даних
    # Наприклад, повернути None, якщо користувач не знайдений або пароль невірний
    # Інакше повернути об'єкт користувача (наприклад, словник)
    if username == "test" and password == "testpass":  # ТЕСТОВИЙ ПРИКЛАД
        return {"username": "test"}
    return None

@app.post(settings.token_url)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Приклад захищеного маршруту
@app.get("/secure-endpoint")
async def read_secure_data(token: str = Depends(oauth2_scheme)):
    # Використайте decode_access_token, якщо потрібно перевірити токен
    # Наприклад: user = decode_access_token(token)
    return {"message": "This is a secure endpoint"}
