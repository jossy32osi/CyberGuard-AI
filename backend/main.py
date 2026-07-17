from fastapi import FastAPI

from backend.database import Base
from backend.database import engine

from backend.models.user import User
from backend.routes import users
from backend.routes import protected
from backend.routes import threats
from backend.routes import virustotal
from backend.routes import abuseipdb
from backend.routes import nvd


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CyberGuard AI",
    description="AI-powered Cybersecurity Platform",
    version="1.0.0"
)


app.include_router(users.router)
app.include_router(protected.router)
app.include_router(threats.router)
app.include_router(virustotal.router)
app.include_router(abuseipdb.router)
app.include_router(nvd.router)

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
