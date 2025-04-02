from hashlib import sha256
from sqlite3 import IntegrityError

from database import SqliteContext

from auth.schema import UserForm

LOGGED_IN_USERS = set()


def create_user(user: UserForm) -> None:
    password_hash = sha256(user.password.encode("utf-8")).hexdigest()

    create_new_user = """INSERT INTO USER (username, full_name, email, password) VALUES (?, ?, ?, ?)"""

    with SqliteContext() as cursor:
        try:
            result = cursor.execute(
                create_new_user,
                (user.username, user.full_name, user.email, password_hash),
            )
            result = result.fetchone()
        except IntegrityError:
            raise IntegrityError

    return result


def verify_user(username: str) -> dict:
    check_user = """SELECT id, password FROM USER WHERE username=(?)"""

    with SqliteContext() as cursor:
        result = cursor.execute(check_user, (username,))
        user = result.fetchone()

    return user
