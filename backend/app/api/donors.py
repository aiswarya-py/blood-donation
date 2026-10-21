from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.database.session import get_db
from app.schemas import DonorCreate,DonorOut
from app.services import donor_service
from app.api.auth import get_user_from_token

router = APIRouter(prefix="/donors",tags=["Donors"])

@router.post("/",response_model=DonorOut)
def create(donor:DonorCreate,token:str,db:Session=Depends(get_db)):
    current_user=get_user_from_token(token)
    existing=donor_service.get_donor_by_phone(db,donor.phone)
    if existing:
        raise HTTPException(status_code=400,detail="Phone number already registered")
    return donor_service.create_donor(db,donor,user_id=current_user["id"])

@router.get("/",response_model=list[DonorOut])
def get_all(db:Session=Depends(get_db)):
    return donor_service.get_all_donors(db)

@router.get("/{donor_id}",response_model=DonorOut)
def get_one(donor_id:int,db:Session =Depends(get_db)):
    donor=donor_service.get_donor_by_id(db,donor_id)
    if not donor:
        raise HTTPException(status_code=404,detail="Donor not found")
    return donor

@router.put("/{donor_id}",response_model=DonorOut)
def update(donor_id:int,donor_data:DonorCreate,db:Session=Depends(get_db)):
    donor = donor_service.update_donor(db,donor_id,donor_data)
    if not donor:
        raise HTTPException(status_code=404,detail="Donor not found")
    return donor

@router.delete("/{donor_id}",response_model=DonorOut)
def soft_delete(donor_id:int,db:Session=Depends(get_db)):
    donor=donor_service.delete_donor(db,donor_id)
    if not donor:
        raise HTTPException(status_code=404,detail="Donor not found")
    return donor
           
