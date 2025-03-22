import unittest
import os

import src.db_utils as db_utils
import src.utils as utils


class TestUtils(unittest.TestCase):
    def test_hash_len_eq_to60(self):
        test_pwd = 'strongpwd1'
        hash_value = utils.generate_hash(test_pwd)
        self.assertTrue(hash_value)
        self.assertEqual(len(hash_value), 60)
    
    def test_hash_uniqueness(self):
        password1 = "test_password1"
        password2 = "test_password2"
        hash1 = utils.generate_hash(password1)
        hash2 = utils.generate_hash(password2)
        self.assertNotEqual(hash1, hash2)
    
    def test_hash_comparison(self):
        password = "test_password"
        hash_value = utils.generate_hash(password)
        self.assertTrue(utils.check_password(hash_value, password))
    
    def test_wrong_password(self):
        password = "test_password"
        wrong_password = "wrong_password"
        hash_value = utils.generate_hash(password)
        self.assertFalse(utils.check_password(hash_value, wrong_password))

    def test_valid_usernames(self):
        valid_cases = [
            "john_doe-123",
            "Alice99",
            "a-b_c",
            "x" * 64
        ]
        for username in valid_cases:
            with self.subTest(username=username):
                self.assertTrue(utils.validate_username(username))

    def test_invalid_usernames(self):
        invalid_cases = [
            "  whitespace  ",
            "user@name",
            "a",
            "x" * 65,
            "user$name",
            ""
        ]
        for username in invalid_cases:
            with self.subTest(username=username):
                self.assertFalse(utils.validate_username(username))
    
    def test_add_user_via_utils(self):
        os.environ['ENVIRONMENT'] = 'testing'
        conn = db_utils.get_db_connection()
        # cursor = self.conn.cursor()
        db_utils.create_table(conn)

        # Add a test user
        username = "test_user"
        password = "test_password"
        password_hash = utils.generate_hash(password)
        result = utils.add_user(conn, username, password_hash)
        self.assertTrue(result)
        conn.close()
        del os.environ['ENVIRONMENT']


if __name__ == '__main__':
    unittest.main()