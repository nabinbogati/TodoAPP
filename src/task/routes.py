import fastapi
from dependencies import LoginDep
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from task import crud
from task.schema import Task

task_router = APIRouter()


@task_router.get(
    "/tasks",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=list,
)
async def get_all_tasks(logged_in: LoginDep):
    if not logged_in:
        return {
            "detail": "User not authorized",
        }
    return crud.get_tasks()


@task_router.get(
    "/tasks/{task_id}",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Task | list,
)
async def get_single_task(task_id: int, logged_in: LoginDep):
    if not logged_in:
        return {
            "detail": "User not authorized",
        }
    return crud.get_tasks(task_id)


@task_router.post(
    "/tasks",
    status_code=fastapi.status.HTTP_201_CREATED,
    response_model=None,
)
async def create_tasks(tasks: list[Task], logged_in: LoginDep) -> Response:
    if not logged_in:
        return JSONResponse(content={"detail": "User not authorized"})
    crud.add_tasks(tasks)
    return JSONResponse(content={"success": True})


# @task_router.put("/tasks/{task_id}", status_code=fastapi.status.HTTP_200_OK)
# async def replace_task(task_id: int, task: Task):
#     pass


# @task_router.patch("/tasks/{task_id}", status_code=fastapi.status.HTTP_200_OK)
# async def update_task(task_id: int, task: Task):
#     pass
