from typing import Annotated, Any

from database import SessionDep
from fastapi import APIRouter, Form, HTTPException
from starlette.responses import JSONResponse

from auth import crud
from auth.crud import get_user_from_email
from auth.models import UserCreate, UserLogin, UserPublic
from auth.security import generate_oauth_tokens, verify_password

auth_router = APIRouter()


@auth_router.post("/auth/register", response_model=UserPublic)
async def register_user(
    session: SessionDep, user_in: Annotated[UserCreate, Form()]
) -> Any:
    user = get_user_from_email(session, user_in.email)
    if user:
        raise HTTPException(
            status_code=400, detail="User with this email already exists in the system."
        )

    user = crud.create_user(session, user_in)
    return user


@auth_router.post("/auth/login")
async def login_user(
    session: SessionDep,
    credentials: Annotated[UserLogin, Form()],
) -> JSONResponse:
    user = crud.get_user_from_email(session, credentials.email)
    if not user:
        raise HTTPException(
            status_code=404, detail="The requested user doesn't exists in the system."
        )

    if not verify_password(credentials.password, user.password):
        raise HTTPException(
            status_code=400, detail="Invalid Credentials, Incorrect Email or Password."
        )

    access_token = generate_oauth_tokens(user.id)
    return JSONResponse(status_code=200, content={"access_token": access_token})
