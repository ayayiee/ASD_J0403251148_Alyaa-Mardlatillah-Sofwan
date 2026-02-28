# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Materi 2 Rekursif : Call Stack
# Tracing Bilangan (Masuk - Keluar)
# Input 3 
# diurai jadi 3-2-1 dan 1-2-3
# Masuk 1-2-3
# Keluar
# ===================================================================

def hitung(n):              # Fungsi rekursif untuk menampilkan proses masuk dan keluar 

    # Base Case
    if n == 0:              # Jika n sudah 0, hentikan rekursi
        print("Selesai.")
        return
    
    print("Masuk: ", n)     # Dieksekusi sebelum recursive call (saat turun)
    # Recursice case
    hitung(n-1)             # Memanggil fungsi dengan n dikurangi 1
    print("Keluar", n)      # Dieksekusi setelah recursive call

print("======== Program Tracing ========")
hitung(3)                   # Memulai rekursi dari n = 3