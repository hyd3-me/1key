import os
import unittest
import src.utils as utils

class TestUtils(unittest.TestCase):
    def test_logger_creation(self):
        logger = utils.setup_logger(environment="testing")
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, "1key")

    def test_log_directory_creation(self):
        utils.setup_logger(environment="production")
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs")
        
        # Check that logs directory exists
        self.assertTrue(os.path.exists(log_dir))
        
        # Check that the log file is created in production mode
        log_file_path = os.path.join(log_dir, "1key.log")
        self.assertTrue(os.path.exists(log_file_path))