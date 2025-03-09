import os
import sqlite3

def get_db_connection():
    # Получаем значение переменной окружения
    environment = os.environ.get("ENVIRONMENT", "development")

    if environment == "testing":
        db_url = ":memory:"
    else:
        db_url = "users.db"

    conn = sqlite3.connect(db_url)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(64),
            password_hash VARCHAR(60)
        )
    ''')
    conn.commit()