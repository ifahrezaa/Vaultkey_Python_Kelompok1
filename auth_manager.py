import json
import hashlib
from pathlib import Path
from tkinter import messagebox

CONFIG_FILE = Path("config.json")

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def load_master():
    if not CONFIG_FILE.exists():
        return None
    with open(CONFIG_FILE, "r") as file:
        data = json.load(file)
        return data.get("master_password")

def save_master(hashed_pw):
    with open(CONFIG_FILE, "w") as file:
        json.dump({"master_password": hashed_pw}, file, indent=4)

def login_user(password):
    stored = load_master()
    if stored is None:
        messagebox.showinfo("Setup", "Belum ada password master, membuat baru...")
        save_master(hash_password(password))
        return True
    if hash_password(password) == stored:
        return True
    messagebox.showerror("Error", "Password salah!")
    return False

def reset_master_password(new_password):
    save_master(hash_password(new_password))
    messagebox.showinfo("Info", "Password master berhasil direset!")
