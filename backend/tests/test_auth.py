from fastapi.testclient import TestClient
from app.main import app
from app.database.session import SessionLocal
from app.models import User

client = TestClient(app)

TEST_EMAIL = "pytest_user@email.com"


def cleanup_test_user(email: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if user:
        db.delete(user)
        db.commit()
    db.close()


def test_register_success():
    cleanup_test_user(TEST_EMAIL)
    response = client.post("/auth/register", json={
        "name": "Pytest User",
        "email": TEST_EMAIL,
        "password": "test12345"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == TEST_EMAIL
    assert "id" in data
    assert "password" not in data


def test_register_duplicate_email():
    response = client.post("/auth/register", json={
        "name": "Pytest User 2",
        "email": TEST_EMAIL,
        "password": "test12345"
    })
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"


def test_login_success():
    response = client.post(f"/auth/login?email={TEST_EMAIL}&password=test12345")
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_login_wrong_password():
    response = client.post(f"/auth/login?email={TEST_EMAIL}&password=wrongpassword")
    assert response.status_code == 401
