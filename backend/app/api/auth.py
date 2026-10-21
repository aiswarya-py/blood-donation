from fastapi import APIRouter,HTTPException,status
from app.schemas.auth import UserCreate,UserOut,Token
from app.services import auth_service
from jose import JWTError

router = APIRouter(prefix="/auth",tags=["Auth"])

users_db = []
user_id_counter =1 
blacklisted_tokens = set()



@router.post("/register",response_model=UserOut)
async def register(user:UserCreate):
    for existing in users_db:
        if existing["email"] == user.email:
            raise HTTPException(status_code=400,detail="Email already registered")

    global user_id_counter
    new_user ={"id":user_id_counter,"name":user.name,"email":user.email,"hashed_password":auth_service.hash_password(user.password)}
    users_db.append(new_user)
    user_id_counter +=1
    return new_user

@router.post("/login",response_model=Token)
async def login(email:str,password:str):
    user=next((user for user in users_db if user["email"] == email),None)
    if not user or not auth_service.verify_password(password,user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")
    token = auth_service.create_access_token({"sub":user["email"]})
    return {"access_token": token, "token_type": auth_service.TOKEN_TYPE}

def get_user_from_token(token:str):
    if token in blacklisted_tokens:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Session expired or invalid token")
    try:
        payload = auth_service.decode_access_token(token)
        email=payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User not found")

    user = next((user for user in users_db if user["email"] == email),None)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User Not found")

    return user 
    

    
