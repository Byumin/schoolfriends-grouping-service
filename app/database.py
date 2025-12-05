from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends
from app.core.config import settings

engine = create_engine(
    settings.db_url, 
    connect_args={"check_same_thread": False} if "sqlite" in settings.db_url else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

CurrentSession = Annotated[Session, Depends(get_db)]