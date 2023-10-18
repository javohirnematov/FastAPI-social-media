from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime


user_router = APIRouter(prefix='/user', tags=['Пользователи'])


# валидация регистрации (То же самое что и Body)
class RegisterModel(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    city: str
    birthday: str
    reg_date: datetime = datetime.now()


# валидация входа в аккаунт (То же самое что и Body)
class LoginModel(BaseModel):
    email: str
    password: str

from registration import registration_api