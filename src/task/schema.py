from datetime import datetime, timezone

from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str = Field(max_length=20)
    description: str = Field(max_length=200)
    created_at: datetime = Field(default=datetime.now(tz=timezone.utc))
