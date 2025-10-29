# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

class FileMetadata(BaseModel):
    id: int
    original_filename: str
    system_filename: str
    file_size_bytes: int
    uploaded_at: datetime

    class Config:
        # Pydantic v1 uses orm_mode, v2 uses from_attributes.
        # If you see a Pydantic warning, change to from_attributes = True
        orm_mode = True
