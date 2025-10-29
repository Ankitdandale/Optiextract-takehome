# 🚀 OptiExtract Takehome Project

---

----------------------------------------------------------------------------------------

## 📖 Overview
This project is a **FastAPI-based web application** that allows users to **upload and manage files** through a simple, lightweight frontend interface.  
It demonstrates basic CRUD operations with FastAPI, SQLite, and Fetch API.

---
----------------------------------------------------------------------------------------

## 🧩 Tech Stack
- **Backend:** FastAPI, SQLAlchemy, SQLite  
- **Frontend:** HTML, CSS, JavaScript (Fetch API)  
- **Server:** Uvicorn  
- **Python:** 3.10+

---
----------------------------------------------------------------------------------------

## ⚙️ Project Setup

### 1️⃣ Clone the Repository
git clone https://github.com/<your-username>/Optiextract-takehome.git
cd Optiextract-takehome

2️⃣ Create Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the FastAPI Server
uvicorn app.main:app --reload
Server runs at:
👉 http://127.0.0.1:8000

----------------------------------------------------------------------------------------

💻 Frontend Pages
Page	Description
frontend/upload.html	Upload new files
frontend/files.html	View & manage uploaded files

----------------------------------------------------------------------------------------

📦 Folder Structure

Optiextract-takehome/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── upload.py
│       └── files.py
│
├── frontend/
│   ├── upload.html
│   └── files.html
│
├── requirements.txt
├── .gitignore
└── README.md
----------------------------------------------------------------------------------------

🧪 Example Run
Start backend:

uvicorn app.main:app --reload

Open frontend:
frontend/upload.html → upload a file

frontend/files.html → view uploaded files

----------------------------------------------------------------------------------------

🧑‍💻 Author
Ankit Digambar Dandale
DevOps & Data Engineer Enthusiast
📍 Pune, Maharashtra
📧 ankitdandale2000@gmail.com
🔗 https://github.com/Ankitdandale/Optiextract-takehome.git

----------------------------------------------------------------------------------------