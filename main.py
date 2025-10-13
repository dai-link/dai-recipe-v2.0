from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
import models, schemas

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/recipes")
def get_recipes(db: Session = Depends(get_db)):
    return db.query(models.Recipe).all()

@app.post("/recipes")
def create_recipe(recipe: schemas.RecipeSchema, db: Session = Depends(get_db)):
    new_recipe = models.Recipe(**recipe.dict())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: schemas.RecipeSchema, db: Session = Depends(get_db)):
    existing_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not existing_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    for key, value in recipe.dict().items():
        setattr(existing_recipe, key, value)
    db.commit()
    db.refresh(existing_recipe)
    return existing_recipe

@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe_to_delete = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not recipe_to_delete:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe_to_delete)
    db.commit()
    return {"message": "Recipe deleted successfully"}

@app.get("/auth")
def get_auth(db: Session = Depends(get_db)):
    return db.query(models.Authorities).all()

@app.post("/auth")
def create_auth(auth: schemas.AuthoritiesSchema, db: Session = Depends(get_db)):
    new_auth = models.Authorities(**auth.dict())
    db.add(new_auth)
    db.commit()
    db.refresh(new_auth)
    return new_auth

@app.put("/auth/{auth_id}")
def update_auth(auth_id: int, auth: schemas.AuthoritiesSchema, db: Session = Depends(get_db)):
    existing_auth = db.query(models.Authorities).filter(models.Authorities.id == auth_id).first()
    if not existing_auth:
        raise HTTPException(status_code=404, detail="Auth not found")
    for key, value in auth.dict().items():
        setattr(existing_auth, key, value)
    db.commit()
    db.refresh(existing_auth)
    return existing_auth

@app.delete("/auth/{auth_id}")
def delete_auth(auth_id: int, db: Session = Depends(get_db)):
    auth_to_delete = db.query(models.Authorities).filter(models.Authorities.id == auth_id).first()
    if not auth_to_delete:
        raise HTTPException(status_code=404, detail="Auth not found")
    db.delete(auth_to_delete)
    db.commit()
    return {"message": "Auth deleted successfully"}

@app.get("/")
def read_root():
    return {"message": "API is running successfully"}


