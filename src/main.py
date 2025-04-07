from auth.routes import auth_router
from database import create_all_databases
from fastapi import FastAPI

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_all_databases()


app.include_router(auth_router)
# app.include_router(task_router)
