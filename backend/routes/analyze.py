from fastapi import APIRouter

from backend.services.threat_service import ThreatService
from backend.core.responses import success_response


router = APIRouter(
    prefix="/analyze",
    tags=["Threat Analysis"]
)


@router.get("/{indicator}")
def analyze(indicator: str):

    result = ThreatService.analyze(indicator)

    return success_response(
        result,
        "Threat analysis completed"
    )
