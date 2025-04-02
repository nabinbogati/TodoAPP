# User schema

user_schema = """
    CREATE TABLE IF NOT EXISTS USER (
        id INTEGER PRIMARY KEY,
        username VARCHAR(12) UNIQUE,
        full_name VARCHAR(33),
        email VARCHAR(33) UNIQUE,
        password VARCHAR(64)
    )
"""
