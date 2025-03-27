from database import SqliteContext
from schema import Task


def add_tasks(tasks: list[Task]):
    query = """ INSERT INTO TASKS (title, description) VALUES (?, ?) """
    data = [(task.title, task.description) for task in tasks]

    with SqliteContext() as cursor:
        cursor.executemany(query, data)


def get_tasks(task_id: int | None = None) -> list:
    query = """ SELECT * FROM TASKS"""

    if task_id:
        query = f""" SELECT * FROM TASKS WHERE id={task_id}"""

    with SqliteContext() as cursor:
        tasks = cursor.execute(query).fetchall()

    return tasks
