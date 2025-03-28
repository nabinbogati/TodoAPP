# create task table

task_schema = """
    CREATE TABLE IF NOT EXISTS TASKS(
        id INTEGER PRIMARY KEY,
        title VARCHAR(30),
        description VARCHAR(100),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""
