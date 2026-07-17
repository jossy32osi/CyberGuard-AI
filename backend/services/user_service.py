from sqlalchemy.orm import Session

from backend.models.user import User
from backend.security.auth import hash_password


class UserService:

    @staticmethod
    def create_user(db: Session, user):

        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password)
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
