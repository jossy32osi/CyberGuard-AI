import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # API Keys
    VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
    ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")

    # Database
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "sqlite:///./cyberguard.db"
    )

    # Authentication
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-before-production"
    )

    ALGORITHM = os.getenv(
        "ALGORITHM",
        "HS256"
    )

    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv(
            "ACCESS_TOKEN_EXPIRE_MINUTES",
            30
        )
    )


settings = Settings()
