from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta


from backend.core.config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(
    plain_password,
    hashed_password
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_access_token(data: dict):
    token_data = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=30
    )

    token_data.update(
        {"exp": expire}
    )

    return jwt.encode(
        token_data,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
