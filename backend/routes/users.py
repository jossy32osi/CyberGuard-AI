from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.services.user_service import UserService
from backend.database.database import get_db
from backend.models.user import User
from backend.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserLogin
)
from backend.security.auth import (
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", response_model=UserResponse)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return UserService.create_user(
        db,
        user
    )


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()


    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    if not verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    token = create_access_token(
        {
            "sub": db_user.email
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }
