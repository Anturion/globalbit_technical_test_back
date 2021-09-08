import os
from typing import List
from dotenv import load_dotenv
from datetime import datetime, timedelta
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, schemas
from . import models, security
from .database import SessionLocal, engine_azure

load_dotenv()
ACCESS_TOKEN_EXPIRE_DAYS=os.getenv('ACCESS_TOKEN_EXPIRE_DAYS')

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
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_email(db, email=user.email)
    db_user_document = crud.users.get_user_by_document(db, document=user.document)
    if db_user or db_user_document:
        raise HTTPException(status_code=404, detail="User already registered")
    return crud.users.create_user(db=db, user=user)


@app.get("/users/", response_model=schemas.users.User)
def read_users(document: int = 0, db: Session = Depends(get_db)):
    users = crud.users.get_user_by_document(db, document=document)
    return users

@app.post("/login/", response_model=schemas.token.Token)
def login_for_access(user_in_db:schemas.users.UserLogin, db: Session=Depends(get_db)):
    user = security.authenticate_user(db, email=user_in_db.email, password=user_in_db.password)
    if not user:
           raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
    )
    
    data={
        'id': user.id,
        'user': user.names,
        'is_active': user.is_active, 
        }
    access_token_expires = timedelta(days=int(ACCESS_TOKEN_EXPIRE_DAYS))
    access_token = security.create_access_token(
        data, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"} 

@app.post("/payments/")
def update_user_state(payment:schemas.payments.PaymentCreate, db: Session=Depends(get_db)):
    db_payment = crud.payments.create_payment(db, payment)
    #user=crud.users.activate_user(db, payment.email)
    
    if db_payment:
        if db_payment.state.value=='Aprobada':
            user=crud.users.activate_user(db, payment.email)
            if user:
                return db_payment
            raise HTTPException(status_code=404, detail="Something went wrong")
    raise HTTPException(status_code=404, detail="Email not found")

    
    
    