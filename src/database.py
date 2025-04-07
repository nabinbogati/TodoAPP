import sqlite3
from typing import Annotated

from config import settings
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine(settings.SQLITE_URL)


def get_session():
    with Session(engine) as session:
        yield session


def create_all_databases():
    SQLModel.metadata.create_all(engine)


class SqliteContext:
    def __init__(self):
        self.connection = sqlite3.connect(settings.SQLITE_PATH)
        self.cursor = self.connection.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, type, value, traceback):
        if traceback:
            self.connection.rollback()
        else:
            self.connection.commit()

        self.cursor.close()


SessionDep = Annotated[Session, Depends(get_session)]
