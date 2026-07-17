from backend.intelligence.threat_engine import analyze_indicator


def calculate_severity(score: int):

    if score >= 81:
        return "CRITICAL"

    if score >= 61:
        return "HIGH"

    if score >= 31:
        return "MEDIUM"

    return "LOW"


def generate_recommendation(severity: str):

    recommendations = {
        "LOW": "Continue monitoring.",
        "MEDIUM": "Investigate this indicator.",
        "HIGH": "Block and investigate immediately.",
        "CRITICAL": "Isolate affected systems and initiate incident response."
    }

    return recommendations[severity]


def correlate(indicator: str):

    local_result = analyze_indicator(indicator)

    score = local_result["risk_score"]

    severity = calculate_severity(score)

    recommendation = generate_recommendation(severity)

    return {
        "indicator": indicator,
        "severity": severity,
        "risk_score": score,
        "recommendation": recommendation,
        "local_analysis": local_result
    }
