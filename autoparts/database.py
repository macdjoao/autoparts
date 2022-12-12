from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
