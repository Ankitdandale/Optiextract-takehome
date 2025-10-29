from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db
import os, uuid, shutil, datetime
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-document")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    system_filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, system_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_metadata = schemas.FileCreate(
        original_filename=file.filename,
        system_filename=system_filename,
        file_size_bytes=os.path.getsize(file_path),
        uploaded_at=datetime.datetime.now()
    )

    db_file = crud.create_file_record(db, file_metadata)
    return {"message": "File uploaded successfully", "file": db_file.system_filename}


# ✅ NEW ENDPOINT
@app.get("/files")
def get_all_files(db: Session = Depends(get_db)):
    files = crud.get_all_files(db)
    return files
