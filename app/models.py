# app/models.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    original_filename = Column(String, nullable=False)
    system_filename = Column(String, nullable=False, unique=True)
    file_size_bytes = Column(Integer, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
