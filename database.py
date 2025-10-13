from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine("postgresql://postgres@localhost:5432/recipe_db")
SessionLocal = sessionmaker(bind=engine)


