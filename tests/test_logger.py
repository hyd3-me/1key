import os
import unittest
from pathlib import Path

import src.utils as utils

class TestUtils(unittest.TestCase):
    def test_logger_creation(self):
        logger = utils.setup_logger(environment="testing")
        self.assertIsNotNone(logger)
        self.assertEqual(logger.name, "1key")

    def test_log_directory_creation(self):
        utils.setup_logger(environment="production")
        log_dir = Path(__file__).parent.parent / "logs"
        # log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs")
        
        # Check that logs directory exists
        self.assertTrue(log_dir.exists())
        
        # Check that the log file is created in production mode
        log_file_path = log_dir / "1key.log"
        self.assertTrue(log_file_path.exists())