# ===============================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
#================================================

# ===============================================
# Latihan 5: Melengkapi fungsi merge
#================================================

def merge(left, right):
    result = []
    i = 0
    j = 0 

    # Bandingkan elemen kiri dan kanan selama keduanya masih ada isi
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:                 # Ambil nilai yang lebih kecil (ascending)
            result.append(left[i])              # Masukkan ke result
            i += 1                              # Geser pointer ke kiri
        else:
            result.append(right[j])             # Masukkan ke result 
            j += 1                              # Geser pointer ke kanan

    # Jika masih ada sisa elemen di kiri, tambahkan semua
    result.extend(left[i:])

    # Jika masih ada sisa elemen di kanan, tambahkan semua
    result.extend(right[j:])

    return result 

# ====================
# Panggil Program 
# ====================

left = [8, 14, 5]
right = [1, 7, 10, 45, 15]
hasil = merge(left, right)
print("Hasil Sorting: ", hasil)


"""
1. Jelaskan fungsi result.extend()
fungsi tersebut berfungsi untuk menambahkan sisa elemen yang belum diproses ke dalam list result.
Hal ini dilakukan agar semua elemen tetap masuk ke hasil akhir setelah proses
perbandingan selesai.
Pada proses penggabungan (merge), perbandingan elemen dilakukan 
selama kedua list masih memiliki elemen. Namun, sering kali salah satu list akan lebih dulu habis. 
Oleh karena itu, elemen yang masih tersisa di list lainnya harus tetap dimasukkan ke dalam result agar tidak hilang.
Metode extend() menambahkan seluruh elemen yang tersisa sekaligus ke dalam list result. 
Berbeda dengan append() yang hanya menambahkan satu elemen, extend() akan menambahkan semua isi list yang diberikan. 
Dengan demikian, result.extend() memastikan seluruh data tergabung secara lengkap dan tetap dalam urutan yang benar.
"""
