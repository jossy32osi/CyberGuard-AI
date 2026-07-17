from fastapi import FastAPI

from backend.database import Base
from backend.database import engine

from backend.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CyberGuard AI",
    description="AI-powered Cybersecurity Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CyberGuard AI",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "database": "Connected",
        "status": "Healthy"
    }
