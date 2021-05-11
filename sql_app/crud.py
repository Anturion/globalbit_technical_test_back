from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_document(db: Session, document: int):
    return db.query(models.User).filter(models.User.document == document).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        document=user.document, name=user.name, phone_number=user.phone_number, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
