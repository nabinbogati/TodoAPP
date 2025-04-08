from typing import Annotated, Any

from database import SessionDep
from fastapi import APIRouter, Form, HTTPException

from auth import crud
from auth.crud import get_user_from_username
from auth.models import Token, UserCreate, UserLogin, UserPublic
from auth.security import create_access_token, verify_password

auth_router = APIRouter()


@auth_router.post("/auth/register", response_model=UserPublic)
async def register_user(
    session: SessionDep, user_in: Annotated[UserCreate, Form()]
) -> Any:
    user = get_user_from_username(session, user_in.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="User with this username already exists in the system.",
        )

    user = crud.create_user(session, user_in)
    return user


@auth_router.post("/auth/login")
async def login_user(
    session: SessionDep,
    credentials: Annotated[UserLogin, Form()],
) -> Token:
    print(credentials)
    user = crud.get_user_from_username(session, credentials.username)
    if not user:
        raise HTTPException(
            status_code=404, detail="The requested user doesn't exists in the system."
        )

    if not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=400,
            detail="Invalid Credentials, Incorrect username or Password.",
        )

    access_token = create_access_token(user.id)
    return Token(access_token=access_token, token_type="Bearer")
