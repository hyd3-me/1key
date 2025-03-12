import unittest
import os
import sqlite3

import src.db_utils as db_utils


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