from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(tags = ["Authentication"])

@router.get("/auth")
def get_auth(db: Session = Depends(get_db)):
    return db.query(models.Authorities).all()

@router.post("/auth")
def create_auth(auth: schemas.AuthoritiesSchema, db: Session = Depends(get_db)):
    new_auth = models.Authorities(**auth.dict())
    db.add(new_auth)
    db.commit()
    db.refresh(new_auth)
    return new_auth

@router.put("/auth/{auth_id}")
def update_auth(auth_id: int, auth: schemas.AuthoritiesSchema, db: Session = Depends(get_db)):
    existing_auth = db.query(models.Authorities).filter(models.Authorities.id == auth_id).first()
    if not existing_auth:
        raise HTTPException(status_code=404, detail="Auth not found")
    for key, value in auth.dict().items():
        setattr(existing_auth, key, value)
    db.commit()
    db.refresh(existing_auth)
    return existing_auth

@router.delete("/auth/{auth_id}")
def delete_auth(auth_id: int, db: Session = Depends(get_db)):
    auth_to_delete = db.query(models.Authorities).filter(models.Authorities.id == auth_id).first()
    if not auth_to_delete:
        raise HTTPException(status_code=404, detail="Auth not found")
    db.delete(auth_to_delete)
    db.commit()
    return {"message": "Auth deleted successfully"}
