# OOP-PYTHON

NAMA: LENI

NIM: 312410442

## Deskripsi
Program ini merupakan program manajemen data mahasiswa yang dibangun menggunakan Python. Program ini memungkinkan pengguna untuk menambah, mengubah, menghapus, dan mencari data mahasiswa. Data mahasiswa disimpan dalam format JSON, sehingga mudah untuk dibaca dan dikelola.

## Fitur
- Tambah data mahasiswa
- Ubah data mahasiswa
- Hapus data mahasiswa
- Cari data mahasiswa berdasarkan NIM
- Tampilkan semua data mahasiswa

## Struktur Proyek

<img src="image.png">

## Deskripsi Kode

### 1. `data/mahasiswa.py`

File ini berisi definisi kelas `Mahasiswa` yang memiliki atribut `nama`, `nim`, dan `nilai`. Selain itu, terdapat beberapa fungsi untuk mengelola data mahasiswa:

- `tambah_mahasiswa(data_mahasiswa, mahasiswa)`: Menambahkan objek mahasiswa ke dalam daftar.
- `ubah_mahasiswa(data_mahasiswa, nim, nilai_baru)`: Mengubah nilai mahasiswa berdasarkan NIM.
- `hapus_mahasiswa(data_mahasiswa, nim)`: Menghapus mahasiswa dari daftar berdasarkan NIM.
- `cari_mahasiswa(data_mahasiswa, nim)`: Mencari mahasiswa berdasarkan NIM.
- `tampilkan_semua_mahasiswa(data_mahasiswa)`: Menampilkan semua data mahasiswa.

### 2. `view/input_form.py`

File ini berisi fungsi `input_data_mahasiswa()` yang digunakan untuk mengambil input dari pengguna untuk menambah data mahasiswa.

### 3. `view/mahasiswa.py`

File ini berisi fungsi `tampilkan_data_mahasiswa(mahasiswa)` yang digunakan untuk menampilkan informasi mahasiswa.

### 4. `main.py`

File ini adalah file utama yang menjalankan aplikasi. Di dalamnya terdapat fungsi `load_data()` untuk memuat data dari file JSON dan `save_data(data)` untuk menyimpan data ke file JSON. Fungsi `main()` mengatur menu interaksi dengan pengguna.


## Penggunaan
- **Instalasi**: Pastikan Anda memiliki Python terinstal di sistem Anda. Anda dapat mengunduhnya dari [python.org](https://www.python.org/downloads/).

- **Clone Repository**: Clone repositori ini ke mesin lokal Anda menggunakan perintah berikut:
   ```
   git clone https://github.com/arfianda/OOP-PYTHON.git
   cd repo
   ```

- **Jalankan Program**

    ```
    python main.py
    ```

- **Menu Utama**:Setelah program berjalan, Anda akan melihat menu utama dengan pilihan:
    ```
    1. Tambah Data Mahasiswa
    2. Ubah Data Mahasiswa
    3. Hapus Data Mahasiswa
    4. Cari Data Mahasiswa
    5. Tampilkan Semua Data Mahasiswa
    6. Keluar
    ```

- **Input Data**:
    - Ikuti instruksi di layar untuk menginput data mahasiswa.

- **Data Mahasiswa**:
    - Data mahasiswa akan disimpan dalam file `data_mahasiswa.json` di direktori proyek.
    <img src="data_mahasiswa.png">


## Catatan

- Pastikan format data yang dimasukkan sesuai dengan yang diminta (misalnya, nilai harus berupa angka).
- Jika terjadi kesalahan saat memuat atau menyimpan data, aplikasi akan memberikan pesan kesalahan yang sesuai.



