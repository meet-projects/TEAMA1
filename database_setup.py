from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class user(Base):
	_tablename_='user'
	id=column(Integer,primary_key=True)
	first_name=column(String(30))
	last_name=column(string)
	gender=column(String(10))
	email=column(String(60))
	status=column(String(60))
	birthdate=column(Date(60))

class photos(Base):
	_tablename_='photos'
	id=column(Integer,primary_key=True)
	name=column(String(60))
	approval=column(Boolean)


