# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Contoh Backtracking 1 : Kombinasi Biner (n)
# ===================================================================

def biner(n, hasil=""):     # Fungsi rekursif untuk membuat kombinasi bilangan biner sepanjang n
    
    # Base case : jika panjang string sudah n, cetak hasil 
    if len(hasil) == n:
        print(hasil)
        return
    
    # Choose + explore: tambah '0'
    biner(n, hasil + "0")     # Recursive call dengan menambahkan digit 0

    # Choose + explore: tambah '1'
    biner(n, hasil + "1")     # Recursive call dengan menambahkan digit 1 
biner(3)                      # Membentuk semua kombinasi biner sepanjang 3 digit







