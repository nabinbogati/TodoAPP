import uuid

from auth.models import UserPublic
from sqlmodel import Session, select

from task.models import Task, TaskCreate, TaskPublic


def get_tasks(
    session: Session,
    user: UserPublic,
    task_id: uuid.UUID | None = None,
) -> TaskPublic | list[TaskPublic] | None:
    if task_id:
        statement = select(Task).where(Task.id == task_id, Task.user_id == user.id)
        db_tasks = session.exec(statement).first()
    else:
        statement = select(Task).where(Task.user_id == user.id)
        db_tasks = session.exec(statement).fetchall()

    if db_tasks:
        return [TaskPublic.model_validate(db_task) for db_task in db_tasks]

    return []


def add_tasks(session: Session, user: UserPublic, tasks: TaskCreate | list[TaskCreate]):
    tasks_db = Task.model_validate(tasks, update={"user_id": user.id})

    session.add(tasks_db)
    session.commit()
    session.refresh(tasks_db)
