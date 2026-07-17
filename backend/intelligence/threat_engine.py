import re


def analyze_indicator(indicator: str):

    result = {
        "indicator": indicator,
        "type": "unknown",
        "risk_score": 0,
        "status": "clean",
        "findings": []
    }


    # Detect IPv4 address
    ip_pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"


    if re.match(ip_pattern, indicator):
        result["type"] = "ip_address"


    # Detect domain
    elif "." in indicator:
        result["type"] = "domain"


    # Detect hash
    elif len(indicator) in [32, 40, 64]:
        result["type"] = "file_hash"



    # Basic risk scoring

    suspicious_keywords = [
        "malware",
        "phishing",
        "attack",
        "evil",
        "bot"
    ]


    for word in suspicious_keywords:

        if word in indicator.lower():

            result["risk_score"] += 25

            result["findings"].append(
                f"Suspicious keyword detected: {word}"
            )



    if result["risk_score"] >= 50:

        result["status"] = "malicious"

    elif result["risk_score"] > 0:

        result["status"] = "suspicious"


    return result
