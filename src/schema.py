from datetime import datetime, timezone

from pydantic import BaseModel, Field

ID_COUNTER = 0


def counter():
    global ID_COUNTER

    ID_COUNTER += 1
    return ID_COUNTER


class Task(BaseModel):
    task_id: int = Field(default_factory=counter)
    description: str = Field(max_length=200)
    created_at: datetime = Field(default=datetime.now(tz=timezone.utc))
