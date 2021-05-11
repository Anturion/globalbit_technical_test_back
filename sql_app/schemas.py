from typing import List, Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    document: int
    name: str
    phone_number: str
    email: str


class User(BaseModel):
    document: int
    name: str
    phone_number: str
    email: str

    class Config:
        orm_mode = True
