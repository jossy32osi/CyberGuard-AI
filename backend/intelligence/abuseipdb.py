import os
import requests

from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv(
    "ABUSEIPDB_API_KEY"
)


BASE_URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip(ip_address: str):

    headers = {
        "Accept": "application/json",
        "Key": API_KEY
    }


    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90
    }


    response = requests.get(
        BASE_URL,
        headers=headers,
        params=params
    )


    if response.status_code != 200:
        return {
            "error": "Unable to query AbuseIPDB",
            "status_code": response.status_code
        }


    data = response.json()


    result = data["data"]


    return {
        "ip": result["ipAddress"],
        "country": result.get("countryCode"),
        "isp": result.get("isp"),
        "abuse_score": result.get(
            "abuseConfidenceScore"
        ),
        "total_reports": result.get(
            "totalReports"
        ),
        "last_reported": result.get(
            "lastReportedAt"
        )
    }
