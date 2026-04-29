# ==========================================
# Nama : Alyaa Mardlatillah SOfwan
# NIM: J0403251148
# Kleas : TPL B-1
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
# ==========================================

from collections import deque           # import deque untuk struktur data queue (antrian)

graph = { 
    'Rumah': ['Sekolah', 'Toko'], 
    'Sekolah': ['Perpustakaan'], 
    'Toko': ['Pasar'], 
    'Perpustakaan': [], 
    'Pasar': [] 
}


def bfs(graph, start): 
    visited = set()                         # menyimpan node yang sudah dikunjungi
    queue = deque([start])                  # antrian dimulai dari node awal

    visited.add(start)                      # tandai node awal sudah dikunjungi

    while queue:                            # selama antrian tidak kosong
        node = queue.popleft()              # ambil node paling depan (FIFO)
        print(node, end=" ")                # tampilkan node

        for neighbor in graph[node]:        # cek semua tetangga dari node
            if neighbor not in visited:     # jika belum dikunjungi
                visited.add(neighbor)       # tandai sebagai sudah dikunjungi
                queue.append(neighbor)      # masukkan ke antrian

print("BFS dari Rumah:") 
bfs(graph, 'Rumah')                         # panggil fungsi mulai dari 'Rumah'

'''
Penjelasan alur:
Algoritma BFS dimulai dari node awal yaitu "Rumah", yang langsung dimasukkan ke dalam antrian (queue) 
dan ditandai sebagai sudah dikunjungi. Selama antrian masih berisi, program akan mengambil node paling 
depan dari antrian, lalu menampilkannya. Dari node tersebut, semua tetangganya diperiksa satu per satu.
Jika ada yang belum pernah dikunjungi, maka node tersebut akan ditandai sebagai sudah dikunjungi dan 
dimasukkan ke dalam antrian. Setelah itu, proses berlanjut ke node berikutnya dalam antrian dengan cara yang sama. 
Karena BFS menggunakan konsep antrian (FIFO), urutan kunjungan akan melebar terlebih dahulu ke semua node yang 
dekat dari titik awal sebelum berpindah ke node yang lebih jauh. Proses ini terus berjalan sampai antrian kosong, 
yang berarti semua node yang dapat dijangkau sudah dikunjungi. 
Hasil akhirnya adalah urutan penelusuran: Rumah, Sekolah, Toko, Perpustakaan, dan Pasar.

1. Node mana yang dikunjungi pertama?
Rumah, karena itu adalah node awal (start).

2. Mengapa BFS cocok untuk mencari jalur terdekat?
Karena BFS mengeksplorasi graph per level (lapisan), jadi node yang paling dekat dari titik awal akan 
dikunjungi lebih dulu sebelum yang lebih jauh.

3. Apa perbedaan urutan BFS jika struktur graph diubah?
Urutan BFS akan berubah karena Bergantung pada urutan tetangga (neighbor) dalam graph dan
bergantung pada struktur koneksi antar node.

'''