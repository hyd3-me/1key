import unittest

import gen_hash

class TestClass(unittest.TestCase):
    def test_hash_len_eq_to60(self):
        test_pwd = 'strongpwd1'
        hash_value = gen_hash.generate_hash(test_pwd)
        self.assertTrue(hash_value)
        self.assertEqual(len(hash_value), 60)


if __name__ == '__main__':
    unittest.main()