import os
import requests

from dotenv import load_dotenv


load_dotenv()


API_KEY = os.getenv(
    "VIRUSTOTAL_API_KEY"
)


BASE_URL = "https://www.virustotal.com/api/v3"


headers = {
    "accept": "application/json",
    "x-apikey": API_KEY
}


def check_ip(ip_address: str):

    url = f"{BASE_URL}/ip_addresses/{ip_address}"


    response = requests.get(
        url,
        headers=headers
    )


    if response.status_code != 200:
        return {
            "error": "Unable to query VirusTotal",
            "status_code": response.status_code
        }


    data = response.json()


    stats = data["data"]["attributes"]["last_analysis_stats"]


    return {
        "ip": ip_address,
        "malicious": stats.get("malicious"),
        "suspicious": stats.get("suspicious"),
        "harmless": stats.get("harmless"),
        "undetected": stats.get("undetected")
    }
