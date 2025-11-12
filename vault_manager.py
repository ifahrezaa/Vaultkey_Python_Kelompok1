import json
from pathlib import Path
from tkinter import messagebox
from crypto_manager import encrypt_data, decrypt_data

VAULT_FILE = Path("vault_data.json")

def load_vault():
    if VAULT_FILE.exists():
        with open(VAULT_FILE, "r") as file:
            return json.load(file)
    return []

def save_vault(data):
    with open(VAULT_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_account(name, username, password):
    data = load_vault()
    encrypted_pw = encrypt_data(password)
    data.append({
        "name": name,
        "username": username,
        "password": encrypted_pw
    })
    save_vault(data)
    messagebox.showinfo("Sukses", f"Akun '{name}' berhasil disimpan!")

def search_account(keyword):
    data = load_vault()
    result = [d for d in data if keyword.lower() in d["name"].lower()]
    if not result:
        messagebox.showwarning("Hasil", "Tidak ada hasil ditemukan.")
    return result

def delete_account(name):
    data = load_vault()
    new_data = [d for d in data if d["name"].lower() != name.lower()]
    save_vault(new_data)
    messagebox.showinfo("Hapus", f"Akun '{name}' telah dihapus.")