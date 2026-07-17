from fastapi import APIRouter

from backend.services.intelligence_service import IntelligenceService


router = APIRouter(
    prefix="/abuseipdb",
    tags=["AbuseIPDB"]
)


@router.get("/ip/{ip}")
def analyze_ip(ip: str):

    return IntelligenceService.abuse_ipdb(ip)
