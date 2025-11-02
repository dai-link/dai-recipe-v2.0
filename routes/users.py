from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Users
from fastapi.responses import JSONResponse
from jwt import create_access_token
from pydantic import BaseModel

router = APIRouter(tags=["Users"])

class UserCreate(BaseModel):
    name: str
    mobile: str
    email: str
    password: str

class UserLogin(BaseModel):
    mobile_or_email: str
    password: str

# 1. SIGNUP
@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):

    # check if already registered
    existing_user = db.query(Users).filter(
        (Users.email == user.email) | (Users.mobile == user.mobile)
    ).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="User already registered")

    # create new user
    new_user = Users(
        name=user.name,
        mobile=user.mobile,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return JSONResponse(
        status_code=201,  #  correct status code
        content={"message": "User created successfully", "user_id": str(new_user.id)}
    )

# 2. LOGIN
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    # can login by mobile OR email
    db_user = db.query(Users).filter(
        (Users.email == user.mobile_or_email) | (Users.mobile == user.mobile_or_email)
    ).first()

    if not db_user or db_user.password != user.password:
        return JSONResponse(
            status_code=401,
            content={"success": False, "message": "Invalid email/mobile or password"}
        )

    payload = {"user_id": str(db_user.id)}
    token = create_access_token(payload)
    return JSONResponse(status_code=200, content={"access_token": token})