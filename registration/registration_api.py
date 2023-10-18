from registration import user_router, RegisterModel, LoginModel
from database.userservice import add_new_user_db, login_user_db, delete_user_db


# запрос на регистрацию пользователя
@user_router.post('/registr-user')
def registr_user(data: RegisterModel):
    # перевод класса на параметры для функции
    registr_data = data.model_dump()
    result = add_new_user_db(**registr_data)

    return {'status': 1, 'message': result}


# запрос на вход в аккаунт
@user_router.post('/login')
def login_user(data: LoginModel):
    # перевод класса на параметры для функции
    login_data = data.model_dump()
    result = login_user_db(**login_data)

    return {'status': 1, 'message': result}


# запрос на удаление пользователя из базы
@user_router.delete('/delete')
def delete_user(user_id: int):
    result = delete_user_db(user_id)

    return {'status': 1, 'message': result}