import os

from dotenv import load_dotenv

load_dotenv()


class Settings:

    VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

    ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./cyberguard.db"
    )

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-before-production"
    )

    ALGORITHM = "HS256"


settings = Settings()
