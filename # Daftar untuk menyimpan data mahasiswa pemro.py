# Daftar untuk menyimpan data mahasiswa
mahasiswa = []

def tambah(nama, nilai):
    """Menambahkan data mahasiswa ke dalam daftar."""
    mahasiswa.append({"nama": nama, "nilai": nilai})
    print(f"Data {nama} berhasil ditambahkan.")

def tampilkan():
    """Menampilkan semua data mahasiswa."""
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return
    print("Daftar Nilai Mahasiswa:")
    for index, mhs in enumerate(mahasiswa, start=1):
        print(f"{index}. Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

def hapus(nama):
    """Menghapus data mahasiswa berdasarkan nama."""
    global mahasiswa
    _mhs = [mhs for mhs in mahasiswa if mhs["nama"] != nama]
    mahasiswa = _mhs
    print(f"Data {nama} berhasil dihapus.")

def ubah(nama, nilai_baru):
    """Mengubah data mahasiswa berdasarkan nama."""
    for mhs in mahasiswa:
        if mhs["nama"] == nama:
            mhs["nilai"] = nilai_baru
            print(f"Data {nama} berhasil diubah menjadi nilai {nilai_baru}.")
            return
    print(f"Data {nama} tidak ditemukan.")

def menu():
    """Menampilkan menu utama."""
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hapus Data")
        print("4. Ubah Data")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1-5): ")

        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nilai = input("Masukkan nilai mahasiswa: ")
            tambah(nama, nilai)
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            hapus(nama)
        elif pilihan == '4':
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_baru = input("Masukkan nilai baru: ")
            ubah(nama, nilai_baru)
        elif pilihan == '5':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()

