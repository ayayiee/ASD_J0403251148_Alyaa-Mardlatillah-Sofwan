# ===============================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
#================================================

# ===============================================
# Latihan 2: Melengkapi Potongan Kode
#================================================

def insertion_sort_asc(data):
    # Loop mulai dari data ke 2 (indeks array ke 1)
    for i in range(1, len(data)):
        key = data[i]                 # Simpan nilai yang disisipkan
        j = i - 1                     # Indeks elemen terakhir di bagian kiri
        
        # Geser elemen yang lebih besar dari key ke kanan
        while j >=0 and data[j] > key :
            data[j+1] = data[j]
            j -= 1
            
        # Letakkan key di posisi yang benar
        data[j+1] = key

    return data
angka = [14, 10, 15, 8, 5, 36, 54, 22]
print("Hasil Sorting (Ascending) : ", insertion_sort_asc(angka))


# =============
# Descending
# =============

def insertion_sort_desc(data):
    # Loop mulai dari data ke 2 (indeks array ke 1)
    for i in range(1, len(data)):
        
        key = data[i]               # Simpan nilai yang disisipkan
        j = i - 1                   # Indeks elemen terakhir di bagian kiri
        
    # Geser elemen yang lebih kecil dari key ke kanan 
        while j >= 0 and data[j] < key:
            data[j+1] = data[j]
            j -= 1
        
        data[j+1] = key
    return data

angka = [14, 10, 15, 8, 5, 36, 54, 22]
print("Hasil Sorting (Descending) : ", insertion_sort_desc(angka))
