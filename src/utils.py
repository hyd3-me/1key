import bcrypt
import re


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
    return re.match(pattern, username.strip()) is not None