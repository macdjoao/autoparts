from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from utils import SQLALCHEMY_DATABASE_URL

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine('mysql+mysqlconnector://root:@localhost/autoparts')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()