import logging

from fastapi import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("CyberGuard-AI")


class IntelligenceServiceError(Exception):
    """Raised when an external threat intelligence provider fails."""

    def __init__(self, service: str, message: str):
        self.service = service
        self.message = message
        super().__init__(message)


async def intelligence_exception_handler(
    request: Request,
    exc: IntelligenceServiceError,
):
    logger.error("[%s] %s", exc.service, exc.message)

    return JSONResponse(
        status_code=503,
        content={
            "status": "error",
            "service": exc.service,
            "message": exc.message,
        },
    )


async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    logger.exception("Unhandled exception")

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": "An unexpected server error occurred.",
        },
    )
