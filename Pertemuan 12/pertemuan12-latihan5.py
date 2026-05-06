# ===================================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 5 : Studi Kasus dengan Program Shortest Path 
# ====================================================

import heapq

# Representasi graph berbobot (waktu tempuh antar kota)
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak dengan tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan (jarak, node)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak lebih besar dari yang sudah tercatat, skip
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Jika ditemukan jarak lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Node awal
start_node = 'Bogor'

hasil = dijkstra(graph, start_node)

print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")

'''
# Jawaban:
# 1. Node awal yang digunakan adalah Bogor.
#    Karena pada soal diminta mencari jarak terpendek dari Bogor ke kota lainnya.
#
# 2. Node yang memiliki jarak paling kecil dari node awal adalah Depok (jarak = 2).
#    Karena Depok memiliki nilai jarak paling kecil dibanding kota lain dari Bogor.
#
# 3. Node yang memiliki jarak paling besar dari node awal adalah Bandung (jarak = 8).
#    Jalur terpendeknya adalah Bogor -> Depok -> Jakarta -> Bandung atau
#    Bogor -> Depok -> Bandung, dan hasil akhirnya adalah 8.
#
# 4. Cara kerja algoritma Dijkstra pada kasus ini:
#    1) Dimulai dari node awal (Bogor) dengan jarak 0.
#    2) Algoritma akan mengecek semua tetangga terdekat terlebih dahulu (Depok dan Jakarta).
#    3) Kemudian memilih node dengan jarak paling kecil (Depok = 2) untuk diproses berikutnya.
#    4) Dari Depok, algoritma memperbarui jarak ke Jakarta dan Bandung jika lebih kecil.
#    5) Proses ini terus berlanjut sampai semua node sudah mendapatkan jarak terpendek.
#    6) Dijkstra bekerja secara greedy, selalu memilih jalur dengan jarak terkecil sementara.
'''