import bcrypt


def generate_hash(pwd):
    return bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt())

def check_password(stored_hash, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_hash)