import logging

from backend.ai.correlation import correlate


logger = logging.getLogger("CyberGuard-AI")


class ThreatService:


    @staticmethod
    def analyze(indicator: str):

        logger.info(
            f"Threat analysis requested: {indicator}"
        )


        result = correlate(indicator)


        logger.info(
            f"Threat analysis completed: {indicator}"
        )


        return result
