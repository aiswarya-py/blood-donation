from datetime import datetime,timedelta,timezone
from passlib.context import CryptContext
from jose import jwt
from decouple import config
from sqlalchemy.orm import Session
from app.models import User
from app.schemas.auth import UserCreate



SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = config('ACCESS_TOKEN_EXPIRE_MINUTES', cast=int)
TOKEN_TYPE = config('TOKEN_TYPE')

pwd_context =CryptContext(schemes=["bcrypt"],deprecated="auto")


def hash_password(password:str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password:str,hashed_password:str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)

def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(User.email == email).first()

def create_user(db:Session,user:UserCreate):
    new_user =User(name=user.name,email=user.email,hashed_password=hash_password(user.password),)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_access_token(data:dict) ->str:
    to_encode =data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def decode_access_token(token:str) -> dict:
    return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])