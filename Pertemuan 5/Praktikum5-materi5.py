# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Contoh Backtracking 2 : Kombinasi Biner dengan Batas '1' (Pruning)
# ===================================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Fungsi rekursif untuk membuat kombinasi biner sepanjang n
    # dengan batas maksimal jumlah digit '1'

    # Pruning: jika jumlah_1 sudh melewati batas, berhenti
    if jumlah_1 > batas:
        return              # Tidak lanjut karena melanggar batas
    
    # Base case
    if len(hasil) == n:
        print(hasil)        # Cetak dan hentikan rekursi
        return
    
    # Pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)        # Tambah '0', jumlah_1 tetap

    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)    # Tambah '1', jumlah_1 bertambah 1

biner_batas(4, 2)            # Membentuk kombinasi biner 4 digit dengan maksimal 2 angka '1'


































