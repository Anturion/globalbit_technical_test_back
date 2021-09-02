from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.sql.sqltypes import DateTime

from .database import Base


class User(Base):
    __tablename__ = "users"
    

    id = Column(Integer, primary_key=True)
    document = Column(Integer, unique=True, index=True)
    names = Column(String)
    last_names=Column(String)
    phone_number = Column(String, default=True)
    email = Column(String(32), unique=True, index=True)
    adress=Column(String(32))
    birthdate=Column(DateTime)
    password=Column(String(100))
    bank=Column(String(32))
    bank_account=Column(Integer)
    upline_code=Column(String(32))
    suscription_code=Column(String(32), unique=True)
    is_active=Column(Boolean)
    is_admin=Column(Boolean)
    created_at=Column(DateTime)
    updated_at=Column(DateTime)
