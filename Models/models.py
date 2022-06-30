from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime


Base = declarative_base()


class Users(Base):
    __tablename__ = 'users_of_policlinic'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    date_of_birth = Column(DateTime)
    users_disease = relationship('Disease')



class Disease(Base):
    __tablename__ = 'about_diseases'
    id = Column(Integer, primary_key=True)
    disease = Column(String)
    user_id = Column(Integer, ForeignKey("users_of_policlinic.id"))