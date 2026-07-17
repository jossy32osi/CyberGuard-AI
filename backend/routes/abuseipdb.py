from fastapi import APIRouter

from backend.intelligence.abuseipdb import check_ip


router = APIRouter(
    prefix="/abuseipdb",
    tags=["AbuseIPDB"]
)


@router.get("/ip/{ip}")
def analyze_ip(ip: str):

    return check_ip(ip)
