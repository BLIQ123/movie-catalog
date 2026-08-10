import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, SessionLocal, Base
from app import models

# Прямые ссылки с открытого CDN TMDB (The Movie Database)
movies_data = [
    {
        "title": "Интерстеллар",
        "description": "Фильм про путешествия сквозь кротовую нору",
        "genre": "Фантастика",
        "year": 2014,
        "rating": 9.0,
        "poster_url": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"
    },
    {
        "title": "Начало",
        "description": "Вор, крадущий секреты из глубин подсознания во время сна.",
        "genre": "Фантастика",
        "year": 2010,
        "rating": 8.8,
        "poster_url": "https://image.tmdb.org/t/p/w500/edv5CZvWj09upO3219J83S82L8m.jpg"
    },
    {
        "title": "Побег из Шоушенка",
        "description": "Успешный банкир обвинен в убийстве и попадает в одну из самых мрачных тюрем.",
        "genre": "Драма",
        "year": 1994,
        "rating": 9.3,
        "poster_url": "https://image.tmdb.org/t/p/w500/9cqN1311oB8A3A2O1S3pGkg8vP5.jpg"
    },
    {
        "title": "Тёмный рыцарь",
        "description": "Бэтмен поднимает ставки в войне с криминалом и сталкивается с гением хаоса — Джокером.",
        "genre": "Боевик",
        "year": 2008,
        "rating": 9.0,
        "poster_url": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"
    },
    {
        "title": "Криминальное чтиво",
        "description": "Двое бандитов ведут философские беседы в перерывах между разборками.",
        "genre": "Криминал",
        "year": 1994,
        "rating": 8.9,
        "poster_url": "https://image.tmdb.org/t/p/w500/fIE3L1AB3A8.jpg"
    },
    {
        "title": "Бойцовский клуб",
        "description": "Страдающий бессонницей клерк встречает харизматичного продавца мыла.",
        "genre": "Драма",
        "year": 1999,
        "rating": 8.8,
        "poster_url": "https://image.tmdb.org/t/p/w500/bptfVGEQuvOwR3R92A3R3ChP3bd.jpg"
    },
    {
        "title": "Матрица",
        "description": "Хакер Нео узнает, что вся его реальность — это иллюзия, созданная машинами.",
        "genre": "Фантастика",
        "year": 1999,
        "rating": 8.7,
        "poster_url": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"
    },
    {
        "title": "Зелёная миля",
        "description": "История надзирателя в блоке смертников и заключенного с удивительным даром.",
        "genre": "Драма",
        "year": 1999,
        "rating": 8.6,
        "poster_url": "https://image.tmdb.org/t/p/w500/vel9C39fRzZ2jM82X9sX5d3XN8X.jpg"
    },
    {
        "title": "Властелин колец: Возвращение короля",
        "description": "Поход Фродо и Сэма к Роковой Горе подходит к концу.",
        "genre": "Фэнтези",
        "year": 2003,
        "rating": 9.0,
        "poster_url": "https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwL2O31M2yR35p1zd.jpg"
    },
    {
        "title": "Форрест Гамп",
        "description": "История доброго и простодушного парня, который случайно становится частью ключевых событий истории США.",
        "genre": "Драма",
        "year": 1994,
        "rating": 8.8,
        "poster_url": "https://image.tmdb.org/t/p/w500/arw2vcBveWOV3A3333.jpg"
    },
    {
        "title": "Аватар",
        "description": "Бывший морпех отправляется на миссию на живописную и опасную планету Пандора.",
        "genre": "Фантастика",
        "year": 2009,
        "rating": 7.9,
        "poster_url": "https://image.tmdb.org/t/p/w500/k39333.jpg"
    }
]

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Полностью очищаем старые записи, чтобы не было конфликтов
        db.query(models.Movie).delete()
        
        # Добавляем обновлённые данные
        for data in movies_data:
            movie = models.Movie(**data)
            db.add(movie)
            
        db.commit()
        print("База данных успешно перезаполнена постерами TMDB!")
    except Exception as e:
        db.rollback()
        print(f"Ошибка при заполнении: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed()