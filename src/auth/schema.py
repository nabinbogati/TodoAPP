from typing import Annotated

from fastapi import Form
from pydantic import BaseModel
from pydantic.networks import EmailStr


class User(BaseModel):
    username: Annotated[str, Form(min_length=5, max_length=12)]
    email: Annotated[EmailStr, Form(min_length=5, max_length=30)]
    full_name: Annotated[str, Form(min_length=5, max_length=30)]


class UserForm(User):
    password: Annotated[str, Form(min_length=7, max_length=30)]
    re_password: Annotated[str, Form(min_length=7, max_length=30)]
