class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan


class DataMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_data(self, mahasiswa):
        self.mahasiswa_list.append(mahasiswa)

    def hapus_data(self, nim):
        self.mahasiswa_list = [m for m in self.mahasiswa_list if m.nim != nim]

    def ubah_data(self, nim, nama_baru, jurusan_baru):
        for m in self.mahasiswa_list:
            if m.nim == nim:
                m.nama = nama_baru
                m.jurusan = jurusan_baru
                break

    def cari_data(self, nim):
        for m in self.mahasiswa_list:
            if m.nim == nim:
                return m
        return None
