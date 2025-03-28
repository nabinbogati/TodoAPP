from typing import Annotated

from fastapi import APIRouter, Form, UploadFile
from starlette.responses import JSONResponse, Response

from auth import crud
from auth.schema import LoginSchema

auth_router = APIRouter()


@auth_router.post("/auth/register")
async def register_user(
    username: Annotated[str, Form(min_length=5, max_length=12)],
    password: Annotated[str, Form(min_length=7, max_length=30)],
    profile: UploadFile,
) -> Response:
    profile_picture = await profile.read()
    user = crud.create_user(username, password, profile_picture)
    return JSONResponse(content={"user": user})


@auth_router.post("/auth/login")
async def login_user(credentials: Annotated[LoginSchema, Form()]) -> Response:
    user = crud.verify_user(credentials)
    return JSONResponse(content={"user": user})
