import logging


from backend.intelligence.virustotal import check_ip as vt_check
from backend.intelligence.abuseipdb import check_ip as abuse_check
from backend.intelligence.nvd import search_cve


logger = logging.getLogger(
    "CyberGuard-AI"
)


class IntelligenceService:


    @staticmethod
    def virus_total(ip: str):

        try:

            logger.info(
                f"VirusTotal lookup: {ip}"
            )

            return vt_check(ip)


        except Exception as e:

            logger.error(
                f"VirusTotal error: {e}"
            )

            return {
                "status": "error",
                "service": "VirusTotal",
                "message": "Unable to complete lookup"
            }



    @staticmethod
    def abuse_ipdb(ip: str):

        try:

            logger.info(
                f"AbuseIPDB lookup: {ip}"
            )

            return abuse_check(ip)


        except Exception as e:

            logger.error(
                f"AbuseIPDB error: {e}"
            )

            return {
                "status": "error",
                "service": "AbuseIPDB",
                "message": "Unable to complete lookup"
            }



    @staticmethod
    def search_vulnerability(keyword: str):

        try:

            logger.info(
                f"NVD lookup: {keyword}"
            )

            return search_cve(keyword)


        except Exception as e:

            logger.error(
                f"NVD error: {e}"
            )

            return {
                "status": "error",
                "service": "NVD",
                "message": "Unable to complete lookup"
            }
