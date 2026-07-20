import logging
import logging.handlers
import sys
import os


LOG_DIR = "logs"


os.makedirs(
    LOG_DIR,
    exist_ok=True
)


def setup_logging():

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )


    file_handler = logging.handlers.RotatingFileHandler(
        "logs/cyberguard.log",
        maxBytes=5_000_000,
        backupCount=5
    )

    file_handler.setFormatter(formatter)


    console_handler = logging.StreamHandler(
        sys.stdout
    )

    console_handler.setFormatter(formatter)


    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            file_handler,
            console_handler
        ]
    )


logger = logging.getLogger(
    "CyberGuard-AI"
)
