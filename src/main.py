from auth.models import user_schema
from auth.routes import auth_router
from database import SqliteContext
from fastapi import FastAPI
from task.models import task_schema
from task.routes import task_router

app = FastAPI()

app.include_router(task_router)
app.include_router(auth_router)

with SqliteContext() as cursor:
    cursor.execute(task_schema)
    cursor.execute(user_schema)
