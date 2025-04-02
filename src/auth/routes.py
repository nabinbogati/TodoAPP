from hashlib import sha256

from fastapi import APIRouter, Form, HTTPException, status
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from starlette.responses import JSONResponse, Response
from typing_extensions import Annotated

from auth import crud
from auth.schema import UserForm
from auth.service import generate_oauth_tokens

auth_router = APIRouter()


@auth_router.post("/auth/register")
async def register_user(user: Annotated[UserForm, Form()]) -> Response:
    crud.create_user(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={})


@auth_router.post("/auth/login")
async def login_user(
    credentials: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> JSONResponse:
    user_dict = crud.verify_user(credentials.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Invalid Username or Password")

    password_hash = sha256(credentials.password.encode("utf-8")).hexdigest()
    if user_dict[1] != password_hash:
        raise HTTPException(status_code=400, detail="Invalid Username or Password")

    access_token = await generate_oauth_tokens(user_dict[0])
    return JSONResponse(content={"access_token": access_token})
