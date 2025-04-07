from pydantic.networks import EmailStr
from sqlmodel import Session, select

from auth.models import User, UserCreate
from auth.security import get_password_hash

LOGGED_IN_USERS = set()


def get_user_from_email(session: Session, email: EmailStr) -> User | None:
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    return user


def create_user(session: Session, user: UserCreate) -> User:
    user_db = User.model_validate(
        user, update={"password": get_password_hash(user.password)}
    )

    session.add(user_db)
    session.commit()
    session.refresh(user_db)

    return user_db
