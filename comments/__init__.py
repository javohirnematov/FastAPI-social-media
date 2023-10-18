from fastapi import APIRouter

comment_router = APIRouter(prefix='/comments', tags=['Комментарии к публикации'])

from comments import comments_api