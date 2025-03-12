import unittest
import os
import sqlite3

import src.db_utils as db_utils
import src.utils as utils


class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        # Set the environment variable for testing
        os.environ['ENVIRONMENT'] = 'testing'
        self.conn = db_utils.get_db_connection()
        self.cursor = self.conn.cursor()
        db_utils.create_table(self.conn)  # Create the table

    def tearDown(self):
        self.conn.close()
        # Delete the environment variable
        del os.environ['ENVIRONMENT']
    
    def test_connection_success(self):
        # Проверяем, что соединение установлено
        self.assertIsNotNone(self.conn)
    
    def test_table_exists(self):
        # Проверяем, что таблица users существует
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
    
    def test_add_user(self):
        # Add a test user
        username = "test_user"
        password = "test_password"
        password_hash = utils.generate_hash(password)  # Генерируем хеш
        db_utils.add_user(self.conn, username, password_hash)  # Используем функцию из db_utils

        # Verify that the user was added
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], username)  # Verify username