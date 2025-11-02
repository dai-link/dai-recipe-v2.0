from fastapi import FastAPI
from sqlalchemy.orm import Session
from database import engine, Base
from routes import users , recipes

# to create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(recipes.router)









