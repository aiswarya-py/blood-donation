from fastapi.testclient import TestClient
from app.main import app
from app.database.session import SessionLocal
from app.models import User,Donor

client = TestClient(app)

TEST_EMAIL = "pytest_donor_user@email.com"

TEST_PHONE = "9876500000"

def cleanup():
    db=SessionLocal()
    donor=db.query(Donor).filter(Donor.phone == TEST_PHONE).first()
    if donor:
        db.delete(donor)
    user=db.query(User).filter(User.email == TEST_EMAIL).first()
    if user:
        db.delete(user)
    db.commit()
    db.close()

def get_token():
    client.post("/auth/register",json={"name":"Donor Test User","email":TEST_EMAIL,"password":"test12345"})
    response = client.post(f"/auth/login?email={TEST_EMAIL}&password=test12345")
    return response.json()["access_token"]

def test_create_donor():
    cleanup()
    token =get_token()
    response =client.post(f"/donors/?token={token}",json={"name":"Donor Test","age":25,"blood_group":"o+","phone":TEST_PHONE,"city":"chennai","is_available":True})
    assert response.status_code == 200
    data = response.json()
    assert data["phone"] == TEST_PHONE
    assert "id" in data
    assert "user_id" in data 

def test_create_donor_duplicate_phone():
    token =get_token()
    response =client.post(f"/donors/?token={token}",json={"name":"Donor Test 2","age":30,"blood_group":"o+","phone":TEST_PHONE,"city":"chennai","is_available":True})
    assert response.status_code == 400
    assert response.json()["detail"] == "Phone number already registered"

def test_get_all_donors():
    response = client.get("/donors/")
    assert response.status_code == 200
    assert isinstance(response.json(),list)


























