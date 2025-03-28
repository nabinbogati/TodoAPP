from fastapi import FastAPI
from task.routes import router

app = FastAPI()

app.include_router(router)
