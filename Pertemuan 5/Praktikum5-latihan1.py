# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Latihan 1 : Rekursi Pangkat
# ===================================================================

def pangkat(a, n):              # Fungsi rekursif untuk menghitung a^n
    # Base case
    if n == 0:                  # Jika n == 0, hasilnya 1 dan hentikan 
        return 1
    
    # Recursive case
    return a * pangkat(a, n-1)  # Kalikan a dengan hasil pangkat(a, n-1) 

print(pangkat(2, 4))            # Menghitung 2^4 dan memunculkan jawabannya 

"""
~ Diskusi dan jelaskan alur program serta base case dan recursive call. 
Alur program:
Fungsi akan terus memanggil dirinya sendiri dengan nilai n dikurangi 1 sampai mencapai n = 0. 
Setelah itu, haisl dikembalikan bertahap hingga menghasilkan nilai akhir.

Base case:
Terjadi saat n == 0, fungsi mengembalikan 1 sebagai kondisi berhenti.

Recursive call:
Terjadi pada a * pangkat(a, n-1)
Setiap pemanggilan mengurangi nilai n hingga mencapai base case.
"""































