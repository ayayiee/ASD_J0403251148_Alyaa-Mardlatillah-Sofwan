# =============================================================
# TUGAS HAND-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: B-1
# =============================================================

# ------------------------------- 
# Konstanta nama file 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt"

# ------------------------------- 
# Fungsi: Membaca data dari file 
# -------------------------------
def baca_stok(nama_file):
    """ 
    Membaca data stok dari file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    Output: - stok_dict (dictionary) 
    key   = kode_barang 
    value = {"nama": nama_barang, "stok": stok_int} 
    """
    stok_dict = {} 

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip() # gunakan strip() untuk menghilangkan \n 

                if baris == "":
                    continue
                
                parts = baris.split(",") # split(",") untuk memisahkan kolom 
                if len(parts) != 3:
                    continue
                
                kode, nama, stok_str = parts
                try: 
                    stok_int = int(stok_str)
                except ValueError:
                    continue

                stok_dict[kode] = { # simpan ke dictionary 
                    "nama" : nama,
                    "stok" : stok_int
                }
    
    except FileNotFoundError:
        pass

    return stok_dict


# --------------------------------
# Fungsi: Menyimpan data ke file 
# --------------------------------
def simpan_stok(nama_file, stok_dict): 
    """ 
    Menyimpan seluruh data stok ke file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    """ 
    with open(nama_file, "w", encoding="utf-8") as file: 
        for kode in sorted(stok_dict.keys()): # melakukan perulangan pada kode barang yang sudah diurutkan 
            nama = stok_dict[kode]["nama"] 
            stok = stok_dict[kode]["stok"]
            file.write(f"{kode}, {nama}, {stok}\n") #menulis data ke file dengan format ini


# ------------------------------- 
# Fungsi: Menampilkan semua data 
# -------------------------------
def tampilkan_semua(stok_dict):  
    """ 
    Menampilkan semua barang di stok_dict. 
    """ 
    if len(stok_dict) == 0: #cek apakah dict kosong atau tidak
        print("Data Kosong")
        return
    
    print("\n======= Daftar Stok Barang =======")
    print(f"{'Kode': <10} | {'Nama' : <12} | {'Stok' :>5}") # menampilkan header tabel dengan format rata kiri dan kanan
    print("-" * 34) # menampilkan garis pemisah antara header dan isi tabel

    for kode in sorted(stok_dict.keys()):
        nama = stok_dict[kode]["nama"] # mengambil nama barang berdasarkan kode
        stok = stok_dict[kode]["stok"] # mengambil jumlah stok berdasarkan kode
        print(f"{kode:<10} | {nama:<12} | {stok:>5}")


# -------------------------------------
# Fungsi: Cari barang berdasarkan kode 
# -------------------------------------
def cari_barang(stok_dict): 
    """ 
    Mencari barang berdasarkan kode barang. 
    """ 
    kode_cari = input("\nMasukkan Kode Barang: ").strip() #input kode barang dari user dan hapus spasi di awal/akhir

    if kode_cari in stok_dict: # cek apakah kode ada di dict
        nama = stok_dict[kode_cari]["nama"] # mengambil nama barang dari dict berdasarkan kode
        stok = stok_dict[kode_cari]["stok"] # mengambil jumlah stok berdasarkan kode

        print("\n ==== Barang Ditemukan ====")
        print(f"Kode    : {kode_cari}") # menampilkan kode barang
        print(f"Nama    : {nama}") # menampilkan nama
        print(f"Stok    : {stok}\n") # menampilkan stok 
    else: 
        print("\nData Tidak Ditemukan")


# ---------------------------
# Fungsi: Tambah barang baru 
# ---------------------------
def tambah_barang(stok_dict): 
    """ 
    Menambah barang baru ke stok_dict. 
    """ 
    kode = input("Masukkan kode barang baru: ").strip() 
    nama = input("Masukkan nama barang: ").strip()

    if kode in stok_dict: #cek apakah kode barang sudah ada
        print("Kode sudah digunakan.\n")
        return
    
    try:
        stok_awal = int(input("Masukkan stok awal: ")) # meminta input stok awal dan mengubahnya menjadi integer 
    except ValueError: # jika input stok bukan angka
        print("Stok harus berupa angka.\n") 
        return

    if stok_awal < 0: # cek apakah stok bernilai kurang dari 0
        print("Stok tidak boleh kurang dari 0.\n")
        return
        
    stok_dict[kode] = { # menambahkna data barang baru ke dictionary
        "nama" : nama,
        "stok" : stok_awal
        }

    print(f"Barang dengan kode {kode} berhasil ditambahkan.") 



# --------------------------- 
# Fungsi: Update stok barang 
# ---------------------------
def update_stok(stok_dict): 
    """ 
    Mengubah stok barang (tambah atau kurangi). 
    Stok tidak boleh menjadi negatif. 
    """ 
    kode = input("\nMasukkan kode Barang yang akan di-update: ").strip()

    if kode not in stok_dict: # mengecek apakh kode ada, jika tidak maka berhenti
        print("Data yang dicari tidak ditemukan, proses update dihentikan.")
        return
    
    print("Pilih jenis update: ")
    print("1. Tambah stok")
    print("2. Kurangi stok")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    try: #input stok baru dan mengubahnya menjadi angka
        jumlah = int(input("Masukkan jumlah stok baru: ").strip())
    except ValueError: # jika input bukan angka maka fungsi dihentikan
        print("Stok harus berupa angka. Update dihentikan.")
        return
    
    if jumlah < 0: # cek apakah stok bernilai kurang dari 0
        print("Input stok tidak valid. Stok harus lebih dari 0 dan tidak boleh di bawah 0.")
        return

    if pilihan == "1":
        stok_dict[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan.")

    elif pilihan == "2":
        if stok_dict[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh kurang dari 0. Update dibatalkan")
            return
        stok_dict[kode]["stok"] -= jumlah
        print("Stok berhasil dikurangi.")

    else:
        print("Pilihan tidak valid")


# ---------------
# Program Utama 
# ---------------

def main ():
    # membaca data dari file saat program mulai
    stok_barang = baca_stok(NAMA_FILE)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)

        elif pilihan == "2":
            cari_barang(stok_barang)

        elif pilihan == "3":
            tambah_barang(stok_barang)

        elif pilihan == "4":
            update_stok(stok_barang)

        elif pilihan == "5":
            simpan_stok(NAMA_FILE, stok_barang)
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# menjalankan program utama
if __name__ == "__main__":
    main()


