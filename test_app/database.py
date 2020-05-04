# test_app/database.py

import sys
#for creating the mapper code
from sqlalchemy import Column, Integer, String, BigInteger

#for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

#for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

#for configuration
from sqlalchemy import create_engine

#create declarative_base instance
Base = declarative_base()

#we'll add classes here
class Members(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(Integer, nullable=False)
    client_member_id = Column(Integer, nullable=False)
    account_id = Column(Integer, nullable=False)

#creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///test_app.db', echo=True)

Base.metadata.create_all(engine)


