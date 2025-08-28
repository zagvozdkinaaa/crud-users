from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal=sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()

def get_db(): 
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()