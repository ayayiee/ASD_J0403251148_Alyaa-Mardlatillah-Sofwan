# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Latihan 3 : Mencari Nilai Maksimum
# ===================================================================

def cari_maks(data, index=0):       # Fungsi rekursif untuk mencari nilai maksimum dalam list

    # Base Case
    if index == len(data) - 1:      # Jika index sudah di elemen terakhir
        return data[index]          # Kembalikan nilai elemen terakhir
    
    # Recursive Case
    maks_sisa = cari_maks(data, index + 1)      # Panggil fungsi untuk mengecek sisa elemen setelah index sekarang

    if data[index] > maks_sisa:     # Bandingkan elemen sekarang dengan maksimum dari sisa elemen
        return data [index]         # Jika lebih besar, kembalikan elemen sekarang
    else:
        return maks_sisa            # Jika tidak, kembalikan nilai maksimum dari sisa elemen
    
angka = [3, 7, 2, 9, 5]
print("Nilai Maksimum: ", cari_maks(angka))     # Memanggil fungsi 

""" 
~ Diskusi dan jelaskan alur program serta base case dan recursive call.
Alur program:
Fungsi memeriksa elemen dari index awal hingga elemen terakhir secara bertahap. 
Setiap pemanggilan akan mengecek sisa elemen sampai mencapai elemen terakhir.
Setelah itu, nilai dibandingkan satu per satu saat proses kembali (unwinding) untuk 
menentukan nilai terbesar.

Base case: 
Terjadi saat index berada di elemen terakhir (index == len(data)-1).
Pada kondisi ini, fungsi langsung mengembalikan nilai elemen tersebut.

Recursive call:
Terjadi pada cari_maks(data, index + 1). 
Setiap pemanggilan memindahkan index ke kanan untuk mencari maksimum ddari sisa elemen.
"""



































