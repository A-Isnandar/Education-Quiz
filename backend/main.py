from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth, questions, quizzes, admin, students
from app.database import engine, Base
import os  # PENTING: Tambah ini

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Platform Kuis Edukatif", version="1.0.0")

# Update CORS settings
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "*" # SEMENTARA: Izinkan semua origin biar gak error pas testing hosting
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(questions.router, prefix="/api/questions", tags=["questions"])
app.include_router(quizzes.router, prefix="/api/quizzes", tags=["quizzes"])
app.include_router(admin.router, prefix="/api/admin", tags=["admin"])
app.include_router(students.router, prefix="/api/students", tags=["students"])

@app.get("/")
async def root():
    return {"message": "Platform Kuis Edukatif API"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}