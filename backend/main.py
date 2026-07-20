from fastapi import FastAPI

from backend.core.logging import setup_logging, logger
from backend.core.exceptions import (
    global_exception_handler,
    intelligence_exception_handler,
    IntelligenceServiceError,
)

from backend.database.database import Base, engine

from backend.routes import (
    users,
    protected,
    threats,
    virustotal,
    abuseipdb,
    nvd,
    analyze,
)

setup_logging()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CyberGuard AI",
    description="AI-powered Cybersecurity Platform",
    version="1.0.0",
)

app.add_exception_handler(
    Exception,
    global_exception_handler,
)

app.add_exception_handler(
    IntelligenceServiceError,
    intelligence_exception_handler,
)

app.include_router(users.router)
app.include_router(protected.router)
app.include_router(threats.router)
app.include_router(virustotal.router)
app.include_router(abuseipdb.router)
app.include_router(nvd.router)
app.include_router(analyze.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CyberGuard AI",
        "status": "Running",
    }


@app.get("/health")
def health():
    return {
        "database": "Connected",
        "status": "Healthy",
    }


@app.on_event("startup")
def startup_event():
    logger.info("CyberGuard-AI API started successfully")
