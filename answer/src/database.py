import sqlite3
from tasker import Task

DB_FILE = 'my_tasks.db'

def init_db():
    """Инициализирует базу данных, если она ещё не создана."""
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS my_tasks ( id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, description TEXT, status TEXT, due_date DATE, priority TEXT, category TEXT ); """)
        conn.commit()

def save_db(manager):
    """Сохраняет все задачи из менеджера в базу данных."""
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM my_tasks")
        for task in manager.read():
            cur.execute(""" INSERT INTO my_tasks (title, description, status) VALUES (?, ?, ?); """, (task.title, task.description, task.status))
        conn.commit()

def load_db(manager):
    """Загружает задачи из базы данных в менеджер."""
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM my_tasks;")
        rows = cur.fetchall()
        for row in rows:
            task = Task(row[1], row[2])
            task.id = row[0]
            task.status = row[3]
            manager.create(task)