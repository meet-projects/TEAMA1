from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__='user'
	id=Column(Integer,primary_key=True)
	first_name=Column(String(30))
	last_name=Column(String)
	gender=Column(String(10))
	email=Column(String(60))
	status=Column(String(60))
	birthdate=Column(Date)
	

class Photos(Base):
	__tablename__='photos'
	id=Column(Integer,primary_key=True)
	name=Column(String(60))
	approval=Column(Boolean)
	agrees=Column(Integer)
	status = Column(String)



