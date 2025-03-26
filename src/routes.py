from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Query

import crud
from crud import TASKS
from schema import Task

router = APIRouter()


@router.get("/tasks")
async def tasks(
    created_at: Annotated[datetime | None, Query()] = datetime.now(timezone.utc),
) -> dict[int, Task]:
    return TASKS


@router.get("/tasks/{task_id}")
async def get_task(task_id: int) -> Task | dict:
    return TASKS.get(task_id, {})


@router.post("/tasks")
async def create_tasks(tasks: list[Task]):
    return crud.create_tasks(tasks)


@router.put("/tasks/{task_id}")
async def replace_task(task_id: int, task: Task) -> dict[int, Task]:
    return crud.replace_task(task_id, task)


@router.patch("/tasks/{task_id}")
async def update_task(task_id: int, task: Task) -> dict[int, Task]:
    return crud.update_task(task_id, task)
