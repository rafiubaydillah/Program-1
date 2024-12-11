import os
import json
from data.mahasiswa import (
    tambah_mahasiswa, 
    ubah_mahasiswa,
    hapus_mahasiswa,
    cari_mahasiswa,
    tampilkan_semua_mahasiswa,
    Mahasiswa
)
from view.input_form import input_data_mahasiswa
from view.mahasiswa import tampilkan_data_mahasiswa

DATA_FILE = "data_mahasiswa.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            try:
                data = json.load(file)
                return [Mahasiswa(**item) for item in data]
            except json.JSONDecodeError:
                print("Error: File data_mahasiswa.json tidak dapat dibaca. Format tidak valid.")
                return []
            except Exception as e:
                print(f"Error saat memuat data: {e}")
                return []
    return []

def save_data(data):
    # Backup file sebelum menulis
    if os.path.exists(DATA_FILE + ".bak"):
        os.remove(DATA_FILE + ".bak")
    
    if os.path.exists(DATA_FILE):
        os.rename(DATA_FILE, DATA_FILE + ".bak")
        
    try:
        with open(DATA_FILE, "w") as file:
            json.dump([{"nama": m.nama, "nim": m.nim, "nilai": m.nilai} for m in data], file, indent=4)
        print("Data berhasil disimpan.")
    except Exception as e:
        print(f"Error saat menyimpan data: {e}")
        # Kembalikan file dari backup jika terjadi error
        if os.path.exists(DATA_FILE + ".bak"):
            os.rename(DATA_FILE + ".bak", DATA_FILE)
            print("File data telah dipulihkan dari backup.")
        else:
            print("Tidak ada file backup untuk dipulihkan.")

def main():
    data_mahasiswa = load_data()

    while True:
        print("\n--- Menu Utama ---")
        print("1. Tambah Data Mahasiswa")
        print("2. Ubah Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Cari Data Mahasiswa")
        print("5. Tampilkan Semua Data Mahasiswa")
        print("6. Keluar")

        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == "1":
            nama, nim, nilai = input_data_mahasiswa()
            mahasiswa = Mahasiswa(nama, nim, nilai)
            tambah_mahasiswa(data_mahasiswa, mahasiswa)
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            try:
                nilai_baru = float(input("Masukkan nilai baru: "))
                ubah_mahasiswa(data_mahasiswa, nim, nilai_baru)
            except ValueError:
                print("Nilai harus berupa angka.")
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            hapus_mahasiswa(data_mahasiswa, nim)
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang akan dicari: ")
            mahasiswa = cari_mahasiswa(data_mahasiswa, nim)
            if mahasiswa:
                tampilkan_data_mahasiswa(mahasiswa)
            else:
                print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")
        elif pilihan == "5":
            tampilkan_semua_mahasiswa(data_mahasiswa)
        elif pilihan == "6":
            save_data(data_mahasiswa)
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()