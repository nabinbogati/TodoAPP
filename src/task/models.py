# create task table

create_task_query = """
    CREATE TABLE TASKS(
        id INTEGER PRIMARY KEY,
        title VARCHAR(30),
        description VARCHAR(100),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
"""
