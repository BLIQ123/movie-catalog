import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_q8sTYaKS9Ecr@ep-odd-bonus-ay38mhk2.c-5.us-east-2.aws.neon.tech/neondb?sslmode=require"
)

# pool_pre_ping=True перед каждым запросом проверяет соединение
# pool_recycle=300 обновляет соединения каждые 5 минут
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=300
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()