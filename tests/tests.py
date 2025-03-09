import unittest
import os
import sqlite3

from db_module import base_db
import gen_hash


class TestClass(unittest.TestCase):
    def test_hash_len_eq_to60(self):
        test_pwd = 'strongpwd1'
        hash_value = gen_hash.generate_hash(test_pwd)
        self.assertTrue(hash_value)
        self.assertEqual(len(hash_value), 60)
    
    def test_hash_uniqueness(self):
        password1 = "test_password1"
        password2 = "test_password2"
        hash1 = gen_hash.generate_hash(password1)
        hash2 = gen_hash.generate_hash(password2)
        self.assertNotEqual(hash1, hash2)
    
    def test_hash_comparison(self):
        password = "test_password"
        hash_value = gen_hash.generate_hash(password)
        self.assertTrue(gen_hash.check_password(hash_value, password))
    
    def test_wrong_password(self):
        password = "test_password"
        wrong_password = "wrong_password"
        hash_value = gen_hash.generate_hash(password)
        self.assertFalse(gen_hash.check_password(hash_value, wrong_password))


class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        # Устанавливаем переменную окружения для тестирования
        os.environ['ENVIRONMENT'] = 'testing'
        self.conn = base_db.get_db_connection()
        self.cursor = self.conn.cursor()
        base_db.create_table(self.conn)  # Создаем таблицу

    def tearDown(self):
        self.conn.close()
        # Удаляем переменную окружения
        del os.environ['ENVIRONMENT']
    
    def test_connection_success(self):
        # Проверяем, что соединение установлено
        self.assertIsNotNone(self.conn)


if __name__ == '__main__':
    unittest.main()