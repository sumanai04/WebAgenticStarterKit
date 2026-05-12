from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Agentic API",
    description="Backend API for the Next.js frontend",
    version="1.0.0"
)

# Crucial for Next.js to communicate with FastAPI locally
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "healthy", "message": "Python Backend is running"}

@app.get("/api/v1/status")
def api_status():
    """Example endpoint for Next.js to fetch"""
    return {
        "database": "connected",
        "ai_agent": "ready",
        "version": "1.0.0"
    }

# Run with: uvicorn main:app --reload --port 8000