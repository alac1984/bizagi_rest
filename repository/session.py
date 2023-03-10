from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import settings


engine = create_engine(settings.db_uri)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
