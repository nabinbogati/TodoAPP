import crud
import fastapi
from fastapi import APIRouter, Response
from schema import Task
from starlette.responses import JSONResponse

router = APIRouter()


@router.get("/tasks", status_code=fastapi.status.HTTP_200_OK, response_model=list)
async def get_all_tasks():
    return crud.get_tasks()


@router.get(
    "/tasks/{task_id}",
    status_code=fastapi.status.HTTP_200_OK,
    response_model=Task | list,
)
async def get_single_task(task_id: int):
    return crud.get_tasks(task_id)


@router.post("/tasks", status_code=fastapi.status.HTTP_201_CREATED, response_model=None)
async def create_tasks(tasks: list[Task]) -> Response:
    crud.add_tasks(tasks)
    return JSONResponse(content={"success": True})


# @router.put("/tasks/{task_id}", status_code=fastapi.status.HTTP_200_OK)
# async def replace_task(task_id: int, task: Task):
#     pass


# @router.patch("/tasks/{task_id}", status_code=fastapi.status.HTTP_200_OK)
# async def update_task(task_id: int, task: Task):
#     pass
