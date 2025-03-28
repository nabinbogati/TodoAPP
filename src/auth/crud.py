from hashlib import sha256
from sqlite3 import IntegrityError, OperationalError

from database import SqliteContext

from auth.schema import LoginSchema


def create_user(username: str, password: str, profile: bytes) -> None:
    password_hash = sha256(password.encode("utf-8")).hexdigest()

    create_new_user = (
        """INSERT INTO USER (username, password, profile) VALUES (?, ?, ?)"""
    )

    with SqliteContext() as cursor:
        try:
            result = cursor.execute(create_new_user, (username, password_hash, profile))
            result = result.fetchone()
        except IntegrityError:
            raise IntegrityError

    return result


def verify_user(credentials: LoginSchema) -> list:
    password_hash = sha256(credentials.password.encode("utf-8")).hexdigest()

    check_user = """SELECT username FROM USER WHERE username=(?) and password=(?)"""

    with SqliteContext() as cursor:
        try:
            result = cursor.execute(check_user, (credentials.username, password_hash))
            user = result.fetchone()
        except OperationalError:
            raise OperationalError

    return user
