from fastapi import Form, UploadFile
from pydantic import BaseModel
from typing_extensions import Annotated


class LoginSchema(BaseModel):
    username: Annotated[str, Form()]
    password: Annotated[str, Form()]


class RegisterSchema(BaseModel):
    profile: UploadFile
