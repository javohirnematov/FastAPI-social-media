from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Ссылка на базу данных
# SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'                                          # Это база на SQLite следующее на POSTGRES
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database/postgres'             # database название берем из docker-compose 5 строчка

# подключение к базе
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Общий класс для наследования в models
Base = declarative_base()

# Генератор подключений к базе
session = sessionmaker(bind=engine)

# Импорт всех классов
from database import models


def get_db():
    db = session()
    try:
        yield db

    except:
        db.rollback()
        raise

    finally:
        db.close()



