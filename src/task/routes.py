import uuid
from typing import Any

from database import SessionDep
from dependencies import AuthDep
from fastapi import APIRouter, Response, status

from task import crud
from task.models import TaskCreate, TaskPublic

task_router = APIRouter(tags=["tasks"])


@task_router.get("/tasks", response_model=list[TaskPublic])
async def get_all_tasks(
    session: SessionDep, user: AuthDep, task_id: uuid.UUID | None = None
):
    tasks = crud.get_tasks(session, user, task_id)
    return tasks


@task_router.post(
    "/tasks",
    response_model=None,
)
async def create_tasks(
    session: SessionDep,
    user: AuthDep,
    tasks: TaskCreate | list[TaskCreate],
) -> Any:
    crud.add_tasks(session, user, tasks)
    return Response(status_code=status.HTTP_201_CREATED)
