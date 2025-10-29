from sqlalchemy.orm import Session
from app import models, schemas

def create_file_record(db: Session, file: schemas.FileCreate):
    db_file = models.FileMetadata(
        original_filename=file.original_filename,
        system_filename=file.system_filename,
        file_size_bytes=file.file_size_bytes,
        uploaded_at=file.uploaded_at
    )
    db.add(db_file)
    db.commit()
    db.refresh(db_file)
    return db_file

def get_all_files(db: Session):
    return db.query(models.FileMetadata).order_by(models.FileMetadata.uploaded_at.desc()).all()
