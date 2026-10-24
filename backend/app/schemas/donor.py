from pydantic import BaseModel, ConfigDict, field_validator

class DonorCreate(BaseModel):
    name:str
    age:int
    blood_group:str
    phone:str
    city:str
    is_available:bool =True

    @field_validator("phone")
    @classmethod
    def validate_phone(cls,value):
        if not value.isdigit():
            raise ValueError("Phone number must contain only digits")
        if len(value)!=10:
            raise ValueError("phone number must be exactly 10 digits")
        if value[0] not in "6789":
            raise ValueError("Phone number must start with 6,7,8,9")
        return value

class DonorOut(BaseModel):
    id:int
    user_id:int
    name:str
    age:int
    blood_group:str
    phone:str
    city:str    
    is_available:bool

    model_config = ConfigDict(from_attributes=True)

