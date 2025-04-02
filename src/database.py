import sqlite3

from config import settings


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
