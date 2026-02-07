# =========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 1: Membuat Fungsi Load Data
# =========================================================

nama_file = "data_mahasiswa.txt"

# membuat fungsi membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
    data_dict = {} # inisialisasi data dictionary/menyiapkan dict kosong 

    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file: # setiap satu baris di file akan diproses satu per satu
            baris = baris.strip() # menghilangkan karakter baris baru, enter (\n), spasi di awal/akhir baris

            parts = baris.split(",") # memisahkan data
            if len(parts) != 3: # ukan 3 bagian (nim, nama, nilai), maka dilewati dan ke program selanjutnya
                continue
            nim, nama, nilai_str = parts #vnilai_str itu masih bentuk teks
            nilai_int = int(nilai_str) # nilai diubah dari teks menjadi angka
            data_dict[nim] = {"nama": nama, "nilai": nilai_int}
            nim, nama, nilai = baris.split(",") # pecah menjadi data satuan

            # simpan data dalam dictionary (key, value)
            data_dict[nim] = {
                "nama": nama,
                "nilai" : int(nilai)
            }
    return data_dict # fungsi mengembalikan dictionary yang berisi semua data mahasiswa.

# memanggil fungsi baca_data_mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
print ("Jumlah data terbaca ", len(buka_data)) # len = menghitung jumlah yang berhasil dibaca

# =========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 2: Membuat Fungsi Menampilkan Data
# =========================================================

def tampilkan_data(data_dict): # menampilkan data mahasiswa yang disimpan di data_dict

    if len(data_dict) == 0: #
        print("Data Kosong")
        return # menghentikan fungsi supaya kode di bawahnya tidak dijalankan
    
    # membuat header tabel
    print("\n===== Daftar Mahasiswa =====") # \n → pindah baris dulu biar rapi
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    print("-" * 32) # membuat strip 32 kali (garis header)

    '''
    untuk tampilan yang rapi, atur f-string formating
        {'NIM': <10} artinya:
        Tampilkan nim <= rata kiri, lebar 10 karakter
        {"Nama" : <12}
        tampilkan nama rata kiri, lebar kolom 12 karakter
        {'Nilai' :>5}
        tampilkan nilai >= rata kanan, dengan lebar 5 karakter
    '''

    for nim in sorted(data_dict.keys()): # ambil NIM dari data_dict, sorted() -> urutkan NIM dari kecil ke besar
        nama=data_dict[nim]["nama"] # ambil nama mahasiswa
        nilai=data_dict[nim]["nilai"]
        print(f"{nim:<10} | {nama: <12} | {nilai:>5}") # hasilnya jadi tabel yang rapi

# memanggil fungsi menampilkan data
tampilkan_data(buka_data)  


# =========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 3: Membuat Fungsi Mencari Data
# =========================================================

def cari_data(data_dict):
    # mencari data mahasiswa berdasarkan NIM\
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict [nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n ==== Data Mahasiswa Ditemukan ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print('\nData Tidak Ditemukan')

cari_data(buka_data)

# =========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 4: Membuat Fungsi Update Nilai
# =========================================================

def update_nilai(data_dict):
    nim = input("Masukkan NIM Mahasiswa yang akan Di-update: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")

    nilai_lama = data_dict[nim]["nilai"]
    # memasukkan nilai update/baru ke dictionary
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

update_nilai(buka_data)

# =========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 5: Membuat Fungsi Menyimpan Perubahan Data ke File
# =========================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}\n")

simpan_data(nama_file, buka_data)
print("Data Berhasil Disimpan")

# =========================================================
# Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
# Latihan 6: Membuat Fungsi Menyimpan Perubahan Data ke File
# =========================================================

def main():
    # menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True:
    print("\n==== MENU DATA MAHASISWA ====")
    print("1. Tampilkan semua data")
    print("2. Cari data berdasarkan NIM")
    print("3. Update nilai mahasiswa")
    print("4. Simpan data ke file")
    print("0. Keluar")

    pilihan = input("Pilihan menu: ").strip()

    if pilihan == "1":
        tampilkan_data(buka_data)

    elif pilihan == "2":
        cari_data(buka_data)

    elif pilihan == "3":
        update_nilai(buka_data)

    elif pilihan == "4":
        simpan_data(nama_file, buka_data)

    elif pilihan == "0":
        print("Program Selesa")
        break
    else:
        print("Pilihan tidak valid. Coba lagi")    

if __name__ == "__main__":
    main()








































































