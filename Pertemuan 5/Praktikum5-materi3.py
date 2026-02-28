# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Materi 3 Rekursif: Menjumlahkan Elemen List
# ===================================================================

def jumlah_list(data, index=0):     # Fungsi rekursif untuk menjumlahkan seluruh elemen list
    
    # Base Case
    if index == len(data):          # Jika index sudah melewati elemen terakhir
        return 0                    # Kembalikan 0 sebagai nilai awal penjumlahan
    
    # Recursive Case
    return data[index] + jumlah_list(data, index+1)     # Menjumlahkan elemen sekarang dengan hasil penjumlahan sisa elemen

print("========== Program jumlah Data List ==========")
print(jumlah_list([2,4,5]))         # Menghitung 2 + 4 + 5 = 11