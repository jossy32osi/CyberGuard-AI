from backend.intelligence.virustotal import check_ip as vt_check
from backend.intelligence.abuseipdb import check_ip as abuse_check
from backend.intelligence.nvd import search_cve


class IntelligenceService:

    @staticmethod
    def virus_total(ip: str):
        return vt_check(ip)

    @staticmethod
    def abuse_ipdb(ip: str):
        return abuse_check(ip)

    @staticmethod
    def search_vulnerability(keyword: str):
        return search_cve(keyword)
