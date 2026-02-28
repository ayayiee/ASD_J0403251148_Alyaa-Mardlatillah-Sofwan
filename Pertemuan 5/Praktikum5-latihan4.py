# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Latihan 4 : Kombinasi Huruf
# ===================================================================

def kombinasi(n, hasil=""):         # Fungsi rekursif untuk membentuk kombinasi A dan B 

    if len(hasil) == n:             # Base case: jika panjang string sudah n maka cetak kombinasi dan hentikan cabang rekursi
        print(hasil)
        return
    
    kombinasi (n, hasil + "A")      # Tambah huruf A
    kombinasi (n, hasil + "B")      # Tambah huruf B

kombinasi(2)                        # Membentuk kombinasi sepanjang 2 karakter

"""
~ Diskusi dan jelaskan: bagaimana jumlah kombinasi yang dihasilkan. 
Pada setiap langkah rekursi, terdapat 2 pilihan (tambah "A" atau "B") artinya
setiap posisi memiliki 2 kemungkinan dan ada n posisi, maka jumlah kombinasi yang dihasilkan adalah 2^n.
Jadi, jumlah kombinasi bertambah secara eksponensial karena setiap level rekursi bercabang menjadi dua.
"""