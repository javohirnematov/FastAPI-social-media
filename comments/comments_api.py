from fastapi import Body

from datetime import datetime
from comments import comment_router
from database.commentservice import get_exact_post_comment_db, add_new_comment_db, \
                                    delete_exact_comment_db, change_exact_comment_db


# запрос на получение комментарий к посту
@comment_router.get('/exact-post-comment')
async def get_exact_post_comment(post_id: int):
    result = get_exact_post_comment_db(post_id)

    return {'status': 1, 'message': result}


# запрос на добавление комментарий (Body)
@comment_router.post('/add_comment')
async def add_new_comment(post_id: int = Body(...), user_id: int = Body(...),
                          comment_text: str = Body(...)):
    result = add_new_comment_db(post_id=post_id, user_id=user_id, comment_text=comment_text,
                                publish_date=datetime.now())

    return {'status': 1, 'message': result}


# запрос на изменение текста к комментарию (Body)
@comment_router.put('/edit-comment')
async def edit_exact_comment(comment_id: int = Body(...), new_comment_text: str = Body(...)):
    result = change_exact_comment_db(comment_id=comment_id, new_comment_text=new_comment_text)

    return {'status': 1, 'message': result}


# удаление определенного комментария
@comment_router.delete('/delete-comment')
async def delete_exact_comment(comment_id: int):
    result = delete_exact_comment_db(comment_id)

    return {'status': 1, 'message': result}
