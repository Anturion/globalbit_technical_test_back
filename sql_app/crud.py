import random
import string
from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas, security

def get_user(db: Session, user_id: int):
    return db.query(models.User).order_by(models.User.id).offset(0).limit(100).filter_by(models.User.id == user_id)


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_document(db: Session, document: int):
    return db.query(models.User).filter(models.User.document == document).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        document=user.document, 
        names=user.names, 
        last_names=user.last_names,
        phone_number=user.phone_number, 
        email=user.email,
        adress= user.adress,
        birthdate=user.birthdate,
        bank=user.bank,
        bank_account=user.bank_account,
        password=security.get_password_hash(user.password),
        upline_code=user.upline_code,
        suscription_code=( ''.join(random.choice(string.ascii_uppercase) for i in range(10))),
        is_active= False,
        is_admin= False,
        created_at = datetime.now(),
        updated_at = datetime.now()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
