# User schema

user_schema = """
    CREATE TABLE IF NOT EXISTS USER (
        id INTEGER PRIMARY KEY,
        username VARCHAR(12) UNIQUE,
        password VARCHAR(64),
        profile BLOB
    )
"""
