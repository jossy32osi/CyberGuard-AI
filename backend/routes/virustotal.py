from fastapi import APIRouter

from backend.services.intelligence_service import IntelligenceService
from backend.core.responses import success_response


router = APIRouter(
    prefix="/virustotal",
    tags=["VirusTotal"]
)


@router.get("/ip/{ip}")
def analyze_ip(ip: str):

    result = IntelligenceService.virus_total(ip)

    return success_response(
        result,
        "VirusTotal analysis completed"
    )
