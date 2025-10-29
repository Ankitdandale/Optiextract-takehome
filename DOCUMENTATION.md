----------------------------------------------------------------------------------------

# OptiExtract Internship Take-Home Assignment
**Candidate:** Ankit Digambar Dandale  
**Project:** File Uploader and Tracker  
**Tech Stack:** FastAPI, SQLAlchemy, SQLite, HTML, CSS, JavaScript

----------------------------------------------------------------------------------------
---

## 🧩 1. Local Setup Guide

### Step 1: Clone the Repository
git clone <https://github.com/Ankitdandale/Optiextract-takehome.git>
cd Optiextract-takehome
Step 2: Create and Activate Virtual Environment
python3 -m venv venv
source venv/bin/activate
Step 3: Install Dependencies
All dependencies are listed in requirements.txt.
pip install -r requirements.txt
Step 4: Run the Application
uvicorn app.main:app --reload
Step 5: Access the Frontend
Open upload.html in your browser to upload files.
Open file_history.html to view uploaded file history.

----------------------------------------------------------------------------------------

🧠 2. Project Overview
This is a two-page web application that performs the initial document ingestion steps:

Uploads files (any type) to a backend server.

Stores them locally in uploaded_files/ folder.

Saves their metadata (filename, size, timestamp) in a SQLite database.

The backend is built using FastAPI for performance and SQLAlchemy for ORM-based data persistence.

----------------------------------------------------------------------------------------

Folder Structure:

app/
 ├── main.py           → FastAPI routes
 ├── crud.py           → Database operations
 ├── models.py         → SQLAlchemy model
 ├── schemas.py        → Pydantic schemas
 ├── database.py       → DB engine/session
 └── Frontend/         → HTML, CSS, JS files
uploaded_files/        → Uploaded file storage
requirements.txt        → Dependencies list
DOCUMENTATION.md        → This file

----------------------------------------------------------------------------------------

⚙️ 3. Design Choices
a) Unique File Naming
Used Python’s built-in UUID module to generate unique filenames:
system_filename = f"{uuid.uuid4()}_{file.filename}"
This ensures no two files overwrite each other.

b) Synchronization Between File Save & Metadata
First, the file is written to disk (uploaded_files/ folder).

Then, metadata is stored in the SQLite database through SQLAlchemy ORM.

If file save fails → metadata won’t be inserted, ensuring data consistency.

c) Frontend Functionality
upload.html: Allows file upload through a simple form.

file_history.html: Fetches data from /files endpoint and displays it in a table format.

----------------------------------------------------------------------------------------

🧩 4. Challenges & Learnings
CORS Handling

Initially, browser blocked API requests.

Solved by enabling CORS in FastAPI:

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
Database Initialization

Ensured database tables are auto-created using:
python
models.Base.metadata.create_all(bind=engine)
Folder Management

Used os.makedirs() to auto-create upload folder if missing.

Frontend Fetch Integration

Used plain JavaScript fetch() API to post and get data without frameworks.

----------------------------------------------------------------------------------------

🎨 5. Aesthetic & Adaptability Notes
Used minimal CSS for clarity and readability.

UI is clean and easy to navigate.

Responsive layout (tested on desktop browser).

Leveraged AI tools (ChatGPT) for debugging and styling suggestions.

----------------------------------------------------------------------------------------

✅ 6. Final Testing Steps
Start backend: uvicorn app.main:app --reload

Open upload.html → choose a file → click “Upload File”

Check uploaded_files/ → file should appear with unique name.

Open file_history.html → list should display uploaded file details.

Verify entries in optiextract.db reflect metadata.

----------------------------------------------------------------------------------------

🚀 7. Dependencies
fastapi

uvicorn

sqlalchemy

pydantic

python-multipart

(Install using pip install -r requirements.txt)

----------------------------------------------------------------------------------------

🧾 8. Repository Link
GitHub: https://github.com/Ankitdandale/Optiextract-takehome.git

----------------------------------------------------------------------------------------