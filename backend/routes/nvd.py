from fastapi import APIRouter

from backend.services.intelligence_service import IntelligenceService


router = APIRouter(
    prefix="/vulnerabilities",
    tags=["NVD Vulnerability Intelligence"]
)


@router.get("/search/{keyword}")
def search_vulnerability(keyword: str):

    return IntelligenceService.search_vulnerability(keyword)
