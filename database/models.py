from sqlalchemy import Integer, DateTime, Date, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, unique=True)
    city = Column(String)
    birthday = Column(Date)
    profile_photo = Column(String)

    reg_date = Column(DateTime)

# Таблица публикаций
class UserPost(Base):
    __tablename__ = 'user_posts'
    post_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_text = Column(String)
    likes = Column(Integer, default=0)

    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')

# Таблица фотографий к посту
class PostPhoto(Base):
    __tablename__ = 'post_photos'
    photo_id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    photo_path = Column(String)

    post_kf = relationship(UserPost, lazy='subquery')

# Таблица комментариев
class PhostComment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, autoincrement=True, primary_key=True)

    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))

    comment_text = Column(String)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')


