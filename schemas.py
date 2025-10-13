from pydantic import BaseModel
from typing import Optional

class RecipeSchema(BaseModel):
    id: int
    name: str
    ingredients: str
    steps: str
    category: str
    created_by: str
    rating: Optional[float]
    prep_time: Optional[int]
    cook_time: Optional[int]
    servings: Optional[int]
    image_url: Optional[str]
    tags: Optional[str]

    class Config:
        orm_mode = True

class AuthoritiesSchema(BaseModel):
    id: int
    client_id: str
    username: str
    password: str
    role: str
    email: str
    created_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True