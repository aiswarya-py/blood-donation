from fastapi import FastAPI
from app.api import donors,auth
from app.database.session import engine,Base
from app.models import Donor

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blood Donation API",
    description ="API for managing blood donors and blood donation requests",
    version="1.0.0",
)

app.include_router(donors.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message":"Blood Donation API is running!"}