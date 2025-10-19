from sqlalchemy import Column, Integer, String, Float, DateTime, UUID
from datetime import datetime
from database import Base

class Recipe(Base):
    
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(String)
    steps = Column(String)
    category = Column(String)
    created_by = Column(String)
    rating = Column(Float)
    prep_time = Column(Integer)
    cook_time = Column(Integer)
    servings = Column(Integer)
    image_url = Column(String)
    tags = Column(String)

class Users(Base):
    __tablename__  = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mobile = Column(String, index=True)
    user_id = Column(UUID, index=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)