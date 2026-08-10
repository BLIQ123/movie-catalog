from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    genre = Column(String, nullable=True)
    year = Column(Integer, nullable=True)
    rating = Column(Float, nullable=True)
    poster_url = Column(String, nullable=True)  # <-- Новое поле