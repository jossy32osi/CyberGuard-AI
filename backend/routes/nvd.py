from fastapi import APIRouter

from backend.intelligence.nvd import search_cve
from backend.core.responses import success_response


router = APIRouter(
    prefix="/vulnerabilities",
    tags=["NVD Vulnerability Intelligence"]
)


@router.get("/search/{keyword}")
def search(keyword: str):

    result = search_cve(keyword)

    return success_response(
        result,
        "Vulnerability search completed"
    )
