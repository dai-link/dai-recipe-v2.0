from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), default=uuid.uuid4, unique=True, index=True)  
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    mobile = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(DateTime, nullable=False, default=datetime.now)

    