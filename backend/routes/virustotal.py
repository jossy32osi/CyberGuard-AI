from fastapi import APIRouter

from backend.intelligence.virustotal import check_ip


router = APIRouter(
    prefix="/virustotal",
    tags=["VirusTotal"]
)


@router.get("/ip/{ip}")
def analyze_ip(ip: str):

    return check_ip(ip)
