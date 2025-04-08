import uuid
from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


# Shared attributes
# Properties to receive vai API on creation
class TaskCreate(SQLModel):
    title: str = Field(min_length=6, max_length=255)
    description: str = Field(min_length=6)


# Database model, database table inferred from class name
class Task(TaskCreate, table=True):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4, unique=True, index=True, primary_key=True
    )
    user_id: uuid.UUID = Field(index=True, foreign_key="user.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


# Properties to return vai API response, id is always required
class TaskPublic(TaskCreate):
    id: uuid.UUID
    created_at: datetime
