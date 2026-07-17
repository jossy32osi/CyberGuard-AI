from fastapi import APIRouter

from backend.intelligence.nvd import search_cve


router = APIRouter(
    prefix="/vulnerabilities",
    tags=["NVD Vulnerability Intelligence"]
)


@router.get("/search/{keyword}")
def search_vulnerability(keyword: str):

    return search_cve(keyword)
