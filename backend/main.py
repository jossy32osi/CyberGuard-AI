from fastapi import FastAPI

app = FastAPI(
    title="CyberGuard AI",
    description="AI-powered Cybersecurity Platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to CyberGuard AI",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }