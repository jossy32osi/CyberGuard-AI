from fastapi import APIRouter

from backend.intelligence.abuseipdb import check_ip
from backend.core.responses import success_response, error_response


router = APIRouter(
    prefix="/abuseipdb",
    tags=["AbuseIPDB"]
)


@router.get("/ip/{ip}")
def analyze_ip(ip: str):

    result = check_ip(ip)

    if isinstance(result, dict) and "error" in result:
        return error_response(
            "AbuseIPDB analysis failed",
            "AbuseIPDB"
        )

    return success_response(
        result,
        "AbuseIPDB analysis completed"
    )
