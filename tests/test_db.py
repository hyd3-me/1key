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

        # Verify that the user was added
        self.cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], username)  # Verify username