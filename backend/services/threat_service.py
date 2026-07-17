from backend.ai.correlation import correlate


class ThreatService:

    @staticmethod
    def analyze(indicator: str):
        return correlate(indicator)
