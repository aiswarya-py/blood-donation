from sqlalchemy import Column, Integer,String,Boolean,ForeignKey
from app.database.session import Base 

class Donor(Base):
    __tablename__ = "donors"
    id = Column(Integer,primary_key=True,index=True)
    user_id =Column(Integer,ForeignKey("users.id"),nullable=False)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    blood_group = Column(String(5), nullable=False)
    phone = Column(String(15), nullable=False)
    city = Column(String(50), nullable=False)
    is_available =Column(Boolean, default=True)
    is_deleted =Column(String(1),default="N",nullable=False)

    
