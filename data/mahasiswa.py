class Mahasiswa:
    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    def __str__(self):
        return f"{self.nama} ({self.nim}) - Nilai: {self.nilai}"

def tambah_mahasiswa(data_mahasiswa, mahasiswa):
    data_mahasiswa.append(mahasiswa)
    print(f"Data mahasiswa {mahasiswa.nama} berhasil ditambahkan.")

def ubah_mahasiswa(data_mahasiswa, nim, nilai_baru):
    for mahasiswa in data_mahasiswa:
        if mahasiswa.nim == nim:
            mahasiswa.nilai = nilai_baru
            print(f"Data nilai mahasiswa dengan NIM {nim} berhasil diubah.")
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

def hapus_mahasiswa(data_mahasiswa, nim):
    for i, mahasiswa in enumerate(data_mahasiswa):
        if mahasiswa.nim == nim:
            del data_mahasiswa[i]
            print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.")
            return
    print(f"Mahasiswa dengan NIM {nim} tidak ditemukan.")

def cari_mahasiswa(data_mahasiswa, nim):
    for mahasiswa in data_mahasiswa:
        if mahasiswa.nim == nim:
            return mahasiswa
    return None

def tampilkan_semua_mahasiswa(data_mahasiswa):
    if data_mahasiswa:
        print("\n--- Data Mahasiswa ---")
        for mahasiswa in data_mahasiswa:
            print(mahasiswa)
    else:
        print("Tidak ada data mahasiswa.")