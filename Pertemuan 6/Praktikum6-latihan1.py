# ===============================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
#================================================

# ===============================================
# Latihan 1: Memahami Kode Program (Insertion Sort)
#================================================

def insertion_sort(data):
    for i in range (1, len(data)):          # Mulai dari indeks 1 (elemen kedua)
        key = data[i]                       # Simpan nilai yang ingin diposisikan
        j = i - 1                           # Indeks elemen sebelumnya (untuk dibandingkan dengan key)

        while j >= 0 and data[j] > key:     # Selama nilai kiri lebih besar dari key
            data[j + 1] = data [j]          # Geser nilai ke kanan
            j -= 1                          # Mundur ke kiri

        data [j + 1] = key                  # Masukkan key ke posisi yang benar
    return data



'''
1. Mengapa perulangan dimulai dari indeks 1?
karena elemen pertama (indeks 0) dianggap sudah terurut.
algoritma pada kode ini bekerja dengan cara menganggap bagian kiri sudah sorted(terurut) lalu mengambil 
elemen berikutnya kemudian menyisipkannya ke posisi yang benar di bagian yang sudah terurut.
karena jikamulai dari index 0, tidak ada elemen sebelumnya untuk dibandingkan.

2. Apa fungsi variabel key?
Variabel "key" berfungsi untuk menyimpan nilai
sementara dari elemen yang akan dipindahkan.
Saat proses pergeseran terjadi di dalam loop while, nilai pada data[j+1] akan ditimpa oleh 
nilai yang lebih besar. Tanpa menyimpan nilai tersebut di dalam key, maka akan 
kehilangan angka yang ingin diurutkan tadi.

3. Mengapa digunakan while, bukan for?
Karena 3. while lebih efisien di gunakan pada kode ini karena jumlah pergeserannya yang tak pasti.
Loop while memungkinkan kita untuk terus bergerak mundur (ke kiri) 
selama syarat tertentu terpenuhi, yang sulit dilakukan dengan struktur 
for standar dalam konteks penyisipan ini.

4. Operasi apa yang terjadi di dalam while?
4. Operasi yang terjadi di dalam while adalah pergeseran (shifting).
Selama elemen di sebelah kiri (data[j]) lebih besar daripada key, algoritma 
akan menyalin atau menggeser elemen tersebut satu posisi ke kanan (data[j + 1] = data[j]). 
Ini dilakukan untuk "membuka ruang" agar key nantinya bisa disisipkan di posisi yang tepat.
'''