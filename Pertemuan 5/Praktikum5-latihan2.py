# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Latihan 2 : Tracing Rekursi
# ===================================================================

def countdown(n):

    if n == 0:              # Base case: menghentikan rekursi ketika n = 0
        print("Selesai")
        return
    print("Masuk: ", n)     # Dieksekusi sebelum recursive call (saat turun)
    countdown(n-1)          # Recursive call: memanggil fungsi dengan n-1
    print("Keluar: ",n)     # Dieksekusi setelah recursive call (saat kembali naik)
countdown(3)                # Memulai proses rekursi dari n = 3

""" 
~ Diskusi dan jelaskan: Mengapa output 'Keluar' muncul terbalik?
Output "keluar" muncul terbalik karena rekursi menggunakan konsep stack (LIFO: Last In, First Out).
artinya, fungsi yang yerakhir dipanggil akan selesai lebih dulu.
Saat countdown (3) dijalankan dan setelah mencapai base case, program mulai kembali (unwinding).
Proses kembali ini terjadi dari fungsi yang terakhir dipanggil.
"""












