# Membuat objek mahasiswa
mahasiswa1 = Mahasiswa("12345", "John Doe", "Informatika")
mahasiswa2 = Mahasiswa("67890", "Jane Smith", "Sistem Informasi")

# Membuat objek DataMahasiswa
data_mahasiswa = DataMahasiswa()

# Menambahkan data mahasiswa
data_mahasiswa.tambah_data(mahasiswa1)
data_mahasiswa.tambah_data(mahasiswa2)

# Mencari data mahasiswa
mahasiswa_yang_dicari = data_mahasiswa.cari_data("12345")
if mahasiswa_yang_dicari:
    print(f"Nama: {mahasiswa_yang_dicari.nama}, Jurusan: {mahasiswa_yang_dicari.jurusan}")

# Mengubah data mahasiswa
data_mahasiswa.ubah_data("12345", "John Doe Jr.", "Ilmu Komputer")

# Menghapus data mahasiswa
data_mahasiswa.hapus_data("67890")
