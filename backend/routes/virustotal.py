from fastapi import APIRouter

from backend.services.intelligence_service import IntelligenceService


router = APIRouter(
    prefix="/virustotal",
    tags=["VirusTotal"]
)


@router.get("/ip/{ip}")
def analyze_ip(ip: str):

    return IntelligenceService.virus_total(ip)
