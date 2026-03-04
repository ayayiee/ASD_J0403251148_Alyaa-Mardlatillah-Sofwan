# ===============================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
#================================================

# ===============================================
# Latihan 4: Memahami Kode Program (Merge Sort)
#================================================

def merge_sort(data):                   # Fungsi untuk mengurutkan data 
    # base case
    if len(data) <= 1:                  # Jika jumlah elemen 1 atau kurang, data sudah terurut
        return data 

    mid = len(data) // 2                # Menentukan titik tengah untuk membagi list
    left = data[:mid]                   # Membagi bagian kiri
    right = data[mid:]                  # Membagi bagian kanan

    # recursive call
    left_sorted = merge_sort(left)      # Mengurutkan bagian kiri secara rekursif
    right_sorted = merge_sort(right)    # Mengurutkan bagian kanan secara rekursif

    return merge_sort(left_sorted, right_sorted)

"""
1. Apa yang dimaksud dengan base case?
Base case adalah kondisi penghenti pada fungsi rekursif, 
tanpa base case fungsi akan terus memanggil dirinya sendiri tanpa henti. 
di kode ini base case nya adalah:
    if len(data) <= 1:
        return data
dimana jika ukuran data sudah tersisa 1 elemen maka akan dianggap sudah terurut, 
fungsi akan berhenti memecah data dan langsung mengembalikan data.

2. Mengapa fungsi memanggil dirinya sendiri?
Fungsi memanggil dirinya sendiri karena menggunakan konsep rekursi, 
di kode ini recursive call nya adalah:
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
fungsi terus memanggil dirinya sendiri agar proses sorting bisa dilakukan 
secara bertahap hingga mencapai base case

3. Apa tujuan fungsi merge()?
Tujuan fungsi merge() adalah untuk menggabungkan 2 daftar yang sudah 
terurut menjadi satu daftar yang terurut kembali.
"""