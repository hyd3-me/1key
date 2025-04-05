import os
import bcrypt
import re
import logging
from logging.handlers import RotatingFileHandler

import src.db_utils as db_utils

def generate_hash(pwd):
    return bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())

def check_password(stored_hash, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_hash)

def validate_username(username):
    """
    Validate username format:
    - Allows alphanumeric characters, hyphens, and underscores
    - Length between 3 and 64 characters
    - No leading/trailing whitespace
    Returns: bool
    """
    pattern = r"^[a-zA-Z0-9-_]{3,64}$"
    return re.match(pattern, username) is not None

def add_user(conn, username, password_hash):
    if not validate_username(username):
        return False
    return db_utils.add_user(conn, username, password_hash)

def setup_logger(environment="production"):
    """
    Configure and return a logger instance for the application.
    :param environment: "production" or "testing"
    """
    logger = logging.getLogger("1key")
    logger.setLevel(logging.DEBUG if environment == "testing" else logging.INFO)

    # Ensure existing handlers are closed before clearing them
    if logger.hasHandlers():
        for handler in logger.handlers:
            if isinstance(handler, RotatingFileHandler):
                handler.close()  # Explicitly close the file handler
        logger.handlers.clear()

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG if environment == "testing" else logging.WARNING)

    # Create log directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs")
    os.makedirs(log_dir, exist_ok=True)

    # Create file handler with log rotation (only in production)
    if environment == "production":
        log_file_path = os.path.join(log_dir, "1key.log")
        file_handler = RotatingFileHandler(
            log_file_path, maxBytes=5 * 1024 * 1024, backupCount=3
        )
        file_handler.setLevel(logging.INFO)
        logger.addHandler(file_handler)

    # Define log format
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    
    if environment == "production":
        file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    
    return logger