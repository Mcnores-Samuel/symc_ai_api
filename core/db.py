from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL


engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base

def get_db():
    """Dependancy for FastAPI routes"""
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()