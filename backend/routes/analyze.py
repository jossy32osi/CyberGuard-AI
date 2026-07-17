from fastapi import APIRouter

from backend.services.threat_service import ThreatService


router = APIRouter(
    prefix="/analyze",
    tags=["Threat Analysis"]
)


@router.get("/{indicator}")
def analyze(indicator: str):

    return ThreatService.analyze(indicator)
