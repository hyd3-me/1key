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
            username VARCHAR(64) UNIQUE,
            password_hash VARCHAR(64)
        )
    ''')
    conn.commit()

def _add_user(conn, username, password_hash):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?) ", (username, password_hash))
    conn.commit()

def add_user(conn, username, password_hash):
    # Add a new user to the database
    try:
        _add_user(conn, username, password_hash)
        return True
    except sqlite3.IntegrityError:
        # Handle the case when the username already exists
        return False
    except sqlite3.Error as e:
        # Log any other SQLite errors
        print(f"An error occurred: {e}")
        return False