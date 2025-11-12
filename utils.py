import uuid
import hashlib

def generate_id():
    return str(uuid.uuid4())

def hash_string(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()
