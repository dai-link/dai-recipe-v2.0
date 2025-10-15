from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(tags = ["Recipes"])

@router.get("/recipes")
def get_recipes(db: Session = Depends(get_db)):
    return db.query(models.Recipe).all()

@router.post("/recipes")
def create_recipe(recipe: schemas.RecipeSchema, db: Session = Depends(get_db)):
    new_recipe = models.Recipe(**recipe.dict())
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe

@router.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: schemas.RecipeSchema, db: Session = Depends(get_db)):
    existing_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not existing_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    for key, value in recipe.dict().items():
        setattr(existing_recipe, key, value)
    db.commit()
    db.refresh(existing_recipe)
    return existing_recipe

@router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe_to_delete = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
    if not recipe_to_delete:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe_to_delete)
    db.commit()
    return {"message": "Recipe deleted successfully"}