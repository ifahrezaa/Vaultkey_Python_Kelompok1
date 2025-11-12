# 🔐 VaultKey - Sistem Manajemen dan Enkripsi Password (Python)

VaultKey adalah aplikasi berbasis Python yang dirancang untuk **mengamankan data sensitif seperti password dan informasi pribadi**.  
Aplikasi ini mendukung fitur **enkripsi, dekripsi, autentikasi pengguna**, dan **penyimpanan lokal yang terenkripsi**.

---

## 🚀 Fitur Utama

### 🧩 1. Autentikasi Pengguna
- Login menggunakan master password.
- Reset password master.
- Validasi keamanan untuk setiap sesi pengguna.

### 🔒 2. Enkripsi & Dekripsi Data
- Menggunakan **Fernet Encryption (AES 128-bit)** dari library `cryptography`.
- Setiap data disimpan dalam format terenkripsi (`.json`).
- Proses enkripsi otomatis saat data disimpan, dan dekripsi saat dibuka.

### 💾 3. Manajemen Data
- Tambah, ubah, dan hapus data terenkripsi.
- Simpan data akun seperti username, password, dan catatan penting.
- Pencarian data cepat dengan filter nama akun.

### 🎨 4. Antarmuka Grafis (GUI)
- Dibangun menggunakan **Tkinter** dengan tampilan modern (warna menarik & tata letak rapi).
- Dukungan multi-frame untuk login, dashboard, dan pengelolaan data.

### 🧠 5. Fitur Tambahan
- Menu **About** untuk informasi aplikasi.
- Opsi **Show/Hide Password**.
- Dukungan multi-user (jika dikembangkan lebih lanjut).

---
## 🧩 Daftar Branch Fitur

| Branch | Deskripsi |
| :------------ | :----------------------------- |
| **main** | Versi stabil aplikasi |
| **fitur-auth** | Sistem login dan autentikasi |
| **fitur-enkripsi** | Proses enkripsi data |
| **fitur-dekripsi** | Proses dekripsi data |
| **fitur-ui** | Desain tampilan GUI |
| **fitur-utils** | Fungsi tambahan & konfigurasi |

---

## 👥 Anggota Kelompok
- Irgi Fahreza  
- Yusuf Febrianto  
- Desti Listia Sari  
- Fahrul Adi  
- Septian Damar  

---

## 🛠️ Teknologi yang Digunakan
- **Python 3.11**  
- **Tkinter (GUI)**  
- **Cryptography (Enkripsi & Dekripsi)**  
- **JSON (Penyimpanan Data)**  
- **Git + GitHub (Kolaborasi Kode)**  

---

## 📜 Lisensi
Proyek ini bersifat **open-source** dan dikembangkan untuk keperluan akademik.  
Dapat digunakan untuk belajar atau dikembangkan lebih lanjut dengan mencantumkan kredit kepada tim pengembang.  

---

> 💬 **“VaultKey — Simpan Rahasia Anda dengan Aman.”**


## 🗂️ Struktur Proyek

Vaultkey_Python_Kelompok1/
│
├── main.py # File utama untuk menjalankan aplikasi
├── auth_manager.py # Modul autentikasi (login, reset password)
├── encrypt_manager.py # Modul enkripsi data
├── decrypt_manager.py # Modul dekripsi data
├── ui_manager.py # Modul GUI aplikasi
├── utils.py # Fungsi tambahan (helper)
│
├── data/
│ └── vault_data.json # Penyimpanan terenkripsi (otomatis dibuat)
│
├── README.md # Dokumentasi proyek
└── requirements.txt # Daftar dependensi Python



---

## ⚙️ Cara Menjalankan Proyek

### 1️⃣ Clone Repository
```bash
git clone https://github.com/ifahrezaa/Vaultkey_Python_Kelompok1.git
cd Vaultkey_Python_Kelompok1
2️⃣ Install Dependensi
Pastikan kamu sudah punya Python ≥ 3.10, lalu jalankan:

bash
Salin kode
pip install -r requirements.txt
3️⃣ Jalankan Program
bash
Salin kode
python main.py


