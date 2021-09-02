from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas, security
from .database import SessionLocal, engine_azure

models.Base.metadata.create_all(bind=engine_azure)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    db_user_document = crud.get_user_by_document(db, document=user.document)
    if db_user or db_user_document:
        raise HTTPException(status_code=404, detail="User already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=schemas.User)
def read_users(document: int = 0, db: Session = Depends(get_db)):
    users = crud.get_user_by_document(db, document=document)
    return users

@app.post("/login/", response_model=schemas.User)
def login_for_access(user_in_db:schemas.UserLogin, db: Session=Depends(get_db)):
    user = security.authenticate_user(db, email=user_in_db.email, password=user_in_db.password)
    if user:
        if user=='no user':
           raise HTTPException(status_code=400, detail="User dosen´t exist")
        if user=='no verify':
            raise HTTPException(status_code=400, detail="Invalid credentials")
    return user

