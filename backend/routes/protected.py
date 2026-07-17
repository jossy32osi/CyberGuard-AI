from fastapi import APIRouter, Depends

from backend.security.dependencies import get_current_user


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(
    current_user: str = Depends(get_current_user)
):

    return {
        "message": "Welcome to CyberGuard AI Dashboard",
        "user": current_user,
        "access": "Authorized"
    }
