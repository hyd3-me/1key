import bcrypt
import re

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
    db_utils.add_user(conn, username, password_hash)
    return True