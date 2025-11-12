from auth_manager import login_user, reset_master_password
from vault_manager import add_account, search_account, delete_account
from crypto_manager import encrypt_data, decrypt_data
from config_manager import load_config
from utils import generate_id

def main():
    load_config()
    print("=== VaultKey Modular ===")
    print("1. Login")
    print("2. Tambah Akun")
    print("3. Cari Akun")
    print("4. Hapus Akun")
    print("5. Enkripsi Manual")
    print("6. Dekripsi Manual")
    print("7. Reset Password Master")
    print("0. Keluar")

    while True:
        pilih = input("\nPilih menu: ")

        if pilih == "1":
            pw = input("Masukkan password master: ")
            if login_user(pw):
                print("Login berhasil.")
        elif pilih == "2":
            n = input("Nama Akun: ")
            u = input("Username: ")
            p = input("Password: ")
            add_account(n, u, p)
        elif pilih == "3":
            key = input("Masukkan kata kunci pencarian: ")
            hasil = search_account(key)
            for h in hasil:
                print(f"- {h['name']}: {decrypt_data(h['password'])}")
        elif pilih == "4":
            n = input("Nama akun yang ingin dihapus: ")
            delete_account(n)
        elif pilih == "5":
            d = input("Data yang ingin dienkripsi: ")
            print("Hasil:", encrypt_data(d))
        elif pilih == "6":
            d = input("Data terenkripsi: ")
            print("Hasil:", decrypt_data(d))
        elif pilih == "7":
            new_pw = input("Password baru: ")
            reset_master_password(new_pw)
        elif pilih == "0":
            print("Keluar...")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
