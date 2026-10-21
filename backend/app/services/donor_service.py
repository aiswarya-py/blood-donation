from sqlalchemy.orm import Session
from app.models import Donor
from app.schemas import DonorCreate

def get_all_donors(db: Session):
    return db.query(Donor).filter(Donor.is_deleted == "N").all()

def get_donor_by_id(db:Session,donor_id:int):
    return db.query(Donor).filter(Donor.id == donor_id,Donor.is_deleted == "N").first()

def get_donor_by_phone(db:Session,phone:str):
    return db.query(Donor).filter(Donor.phone ==phone,Donor.is_deleted == "N").first()

def create_donor(db:Session, donor:DonorCreate,user_id:int):
    new_donor = Donor(
        user_id=user_id,
        name=donor.name,
        age=donor.age,
        blood_group=donor.blood_group,
        phone=donor.phone,
        city=donor.city,
        is_available=donor.is_available,
        is_deleted="N"
    )
    db.add(new_donor)
    db.commit()
    db.refresh(new_donor)
    return new_donor


def update_donor(db:Session,donor_id:int,donor_data:DonorCreate):
    donor = get_donor_by_id(db, donor_id)  
    if not donor:
        return None
    donor.name = donor_data.name
    donor.age = donor_data.age
    donor.blood_group =donor_data.blood_group
    donor.phone = donor_data.phone
    donor.city = donor_data.city
    donor.is_available =donor_data.is_available
    db.commit()
    db.refresh(donor)
    return donor

def delete_donor(db:Session,donor_id:int):
    donor =get_donor_by_id(db, donor_id)
    if not donor:
        return None
    donor.is_deleted ="Y"
    db.commit()
    db.refresh(donor)
    return donor


