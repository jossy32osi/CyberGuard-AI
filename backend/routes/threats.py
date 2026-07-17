from fastapi import APIRouter

from backend.intelligence.threat_engine import analyze_indicator


router = APIRouter(
    prefix="/threats",
    tags=["Threat Intelligence"]
)


@router.get("/analyze/{indicator}")
def analyze_threat(indicator: str):

    result = analyze_indicator(
        indicator
    )

    return result
