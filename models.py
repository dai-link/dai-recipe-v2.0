from sqlalchemy import Column, Integer, String, Float, DateTime
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

class Authorities(Base):
    __tablename__ = "authorities"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="user")
    email = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    