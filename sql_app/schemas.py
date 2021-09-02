from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    document: int
    names: str
    last_names: str
    phone_number: str
    email: str
    adress: str
    birthdate: datetime
    bank:str=None
    bank_account:int=None
    upline_code:str
    password: str


class User(BaseModel):
    document: int
    names: str
    last_names: str
    phone_number: str
    email: str
    adress: str
    bank:str=None
    bank_account:int=None
    birthdate: datetime
    password: str
    upline_code: str
    suscription_code: str
    is_active: bool=False
    is_admin: bool=False
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserLogin(BaseModel):

    email:str
    password:str