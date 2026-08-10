from sqlalchemy.orm import Session
from . import models, schemas

def get_movies(db: Session, genre: str = None, search: str = None):
    query = db.query(models.Movie)
    if genre:
        query = query.filter(models.Movie.genre.ilike(f"%{genre}%"))
    if search:
        query = query.filter(models.Movie.title.ilike(f"%{search}%"))
    return query.all()

def create_movie(db: Session, movie: schemas.MovieCreate):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie 