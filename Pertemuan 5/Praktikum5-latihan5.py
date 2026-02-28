# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Latihan 5 : Generator PIN
# ===================================================================

def buat_pin(panjang, hasil=""):            # Fungsi rekursif untuk membuat kombinasi PIN
    
    if len(hasil) == panjang:               # Base case: jika panjang PIN sudah sesuai, cetak pin dan hentikan
        print("PIN: ", hasil)
        return
    
    for angka in ["0", "1", "2"]:           # Tiga pilihan angka setiap posisi
        buat_pin(panjang, hasil + angka)    # Recursive call: tambah satu angka


buat_pin(3)                                 # Membuat semua kombinasi PIN sepanjang 3 digit

"""
~ Diskusi dan jelaskan: Bagaimana cara mencegah angka yang sama muncul berulang? 
Untuk mencegah angka yang sama muncul berulang dalam PIN, kita perlu memastikan
bahwa setiap angka hanya digunakan sekali dalam satu kombinasi dengan cara
mengecek apakah angka yang akan ditambahkan sudah ada di dalam string 'hasil'.
Jika sudah ada, maka angka tersebut tidak boleh dipakai lagi.

Bisa tambahkan kode:
if angka not in hasil:
    Buat_pin(panjang, hasil + angka)

Dengan cara ini, setiap kombinasi hanya berisi angka yang unik/tidak perulangan.
Akibatnya, jumlah kombinasi tidak lagi 3^n, melainkan jadi permutasi tanpa perulangan.
"""






