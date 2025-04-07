import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


# Shared user properties
class UserBase(SQLModel):
    full_name: str = Field(max_length=255)
    email: EmailStr = Field(index=True, unique=True, max_length=255)


# Properties to receive vai API on creation
class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=255)
    re_password: str = Field(min_length=6, max_length=255)


class UserLogin(SQLModel):
    email: EmailStr = Field(max_length=255)
    password: str = Field(min_length=6, max_length=255)


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    password: str = Field(min_length=6, max_length=255)


# Properties to return vai API response, id is always required
class UserPublic(UserBase):
    id: uuid.UUID
