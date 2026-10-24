from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas.auth import UserCreate, UserOut, Token
from app.services import auth_service
from jose import JWTError

router = APIRouter(prefix="/auth", tags=["Auth"])

blacklisted_tokens = set()


@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = auth_service.get_user_by_email(db, user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return auth_service.create_user(db, user)


@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = auth_service.get_user_by_email(db, email)
    if not user or not auth_service.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    token = auth_service.create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": auth_service.TOKEN_TYPE}


def get_user_from_token(token: str, db: Session):
    if token in blacklisted_tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Session expired, please login again")
    try:
        payload = auth_service.decode_access_token(token)
        email = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    user = auth_service.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user


@router.get("/me", response_model=UserOut)
def get_me(token: str, db: Session = Depends(get_db)):
    return get_user_from_token(token, db)


@router.post("/logout")
def logout(token: str, db: Session = Depends(get_db)):
    get_user_from_token(token, db)
    blacklisted_tokens.add(token)
    return {"message": "Logged out successfully"}
