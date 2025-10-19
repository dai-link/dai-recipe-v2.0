from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Users
from fastapi.responses import JSONResponse
from jwt import create_access_token

router = APIRouter(tags=["Users"])

@router.get("/login")
def login(user_id: str, db: Session = Depends(get_db)):
    
    db_user = db.query(Users).filter(Users.user_id == user_id).first()

    if not db_user:
        d = {
            "success": True,
            "message": "User not found" 
        }

        return JSONResponse(status_code=404, content=d)
    
    else:

        payload = {
            "user_id": str(db_user.user_id)
        }

        token = create_access_token(payload)

        d = {
            "access_token": token
        }

        return JSONResponse(status_code=200, content=d)