from schema import Task

TASKS = {}


def create_tasks(tasks: list[Task]) -> dict[int, Task]:
    for task in tasks:
        print(task.task_id)
    new_tasks = {task.task_id: task.model_dump() for task in tasks}
    TASKS.update(new_tasks)
    return TASKS


def update_task(task_id: int, task: Task) -> dict[int, Task]:
    if TASKS.get(task_id):
        for key, value in task.model_dump().items():
            TASKS[task_id][key] = value

    return TASKS


def replace_task(task_id: int, task: Task) -> dict[int, Task]:
    if TASKS.get(task_id):
        for key, value in task.model_dump().items():
            TASKS[task_id][key] = value

    return TASKS
