import base64
import json
from cryptography.fernet import Fernet
from pathlib import Path

KEY_FILE = Path("key.json")

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "w") as file:
        json.dump({"key": key.decode()}, file)
    return key

def load_key():
    if not KEY_FILE.exists():
        return generate_key()
    with open(KEY_FILE, "r") as file:
        data = json.load(file)
        return data["key"].encode()

def encrypt_data(data: str) -> str:
    fernet = Fernet(load_key())
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(data: str) -> str:
    fernet = Fernet(load_key())
    return fernet.decrypt(data.encode()).decode()
