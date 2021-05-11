from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    document = Column(String, unique=True, index=True)
    name = Column(String)
    phone_number = Column(String, default=True)
    email = Column(String, unique=True, index=True)
