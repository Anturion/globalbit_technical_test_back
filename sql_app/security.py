import os
from dotenv import load_dotenv
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from . import crud

load_dotenv()

ALGORITHM = os.getenv('ALGORITHM')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db:Session, email:str, password:str):
    user=crud.get_user_by_email(db, email)
    if not user:
        return 'no user'
    if not verify_password(password, user.password):
        return 'no verify'
    return user
