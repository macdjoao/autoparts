from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session

app = FastAPI()


@app.get('/')
def home(db: Session = Depends(get_db)):
    return 'Olá mundo'
