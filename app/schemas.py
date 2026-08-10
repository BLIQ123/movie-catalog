from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    description: str | None = None
    genre: str | None = None
    year: int | None = None
    rating: float | None = None
    poster_url: str | None = None  # <-- Новое поле

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True