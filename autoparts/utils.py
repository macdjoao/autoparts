import os
from dotenv import load_dotenv

SECRET_KEY = str(os.environ.get('SECRET_KEY'))
ALGORITHM = str(os.environ.get('ALGORITHM'))
SQLALCHEMY_DATABASE_URL = str(os.environ.get('SQLALCHEMY_DATABASE_URL'))