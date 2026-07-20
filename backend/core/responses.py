from typing import Any


def success_response(
    data: Any,
    message: str = "Request successful"
):

    return {
        "success": True,
        "message": message,
        "data": data
    }



def error_response(
    message: str,
    error: str = None
):

    response = {
        "success": False,
        "message": message
    }

    if error:
        response["error"] = error

    return response
