from sqlalchemy import Column,Integer,String
from app.database.session import Base 

class User(Base):
    __tablename__="users"

    id =Column(Integer,primary_key=True,index=True)
    name=Column(String(50),nullable=False)
    email=Column(String(100),nullable=False,unique=True)
    hashed_password=Column(String(255),nullable=False)

    