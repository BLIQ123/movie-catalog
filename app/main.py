from fastapi import FastAPI, Depends, Query, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

app = FastAPI(title="Movie Catalog API")

# Разрешаем запросы с любых фронтендов
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API connected to Neon PostgreSQL!"}

# GET с поддержкой фильтров: /api/movies?genre=Фантастика&search=Начало
@app.get("/api/movies", response_model=list[schemas.MovieResponse])
def get_movies(
    genre: str | None = Query(None, description="Фильтр по жанру"),
    search: str | None = Query(None, description="Поиск по названию"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Movie)
    
    if genre:
        query = query.filter(models.Movie.genre.ilike(f"%{genre}%"))
    if search:
        query = query.filter(models.Movie.title.ilike(f"%{search}%"))
        
    return query.all()

@app.post("/api/movies", response_model=schemas.MovieResponse, status_code=status.HTTP_201_CREATED)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    db_movie = models.Movie(**movie.model_dump())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie