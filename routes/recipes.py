from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from jwt import verify_access_token

router = APIRouter(tags=["Recipes"])

# Get all recipes
@router.get("/recipes")
def get_recipes(user_id: str = Depends(verify_access_token),db: Session = Depends(get_db)):
    try:
        recipes = db.query(models.Recipe).all()
        return {"data": recipes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Create new recipe
@router.post("/recipes")
def create_recipe(recipe: schemas.RecipeSchema, db: Session = Depends(get_db)):
    try:
        new_recipe = models.Recipe(**recipe.dict())
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)
        return {"message": "Recipe created successfully", "data": new_recipe}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update existing recipe
@router.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: schemas.RecipeSchema, db: Session = Depends(get_db)):
    try:
        existing_recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
        if not existing_recipe:
            raise HTTPException(status_code=404, detail="Recipe not found")

        for key, value in recipe.dict().items():
            setattr(existing_recipe, key, value)

        db.commit()
        db.refresh(existing_recipe)
        return {"message": "Recipe updated successfully", "data": existing_recipe}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Delete a recipe
@router.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    try:
        recipe_to_delete = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()
        if not recipe_to_delete:
            raise HTTPException(status_code=404, detail="Recipe not found")

        db.delete(recipe_to_delete)
        db.commit()
        return {"message": "Recipe deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

    