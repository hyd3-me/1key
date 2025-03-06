import unittest

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


if __name__ == '__main__':
    unittest.main()