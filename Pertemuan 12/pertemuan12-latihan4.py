# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ===============================================

import heapq 

# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
    'Perpustakaan': {'Lab': 3}, 
    'Kantin': {'Lab': 4, 'Aula': 7}, 
    'Lab': {'Aula': 1}, 
    'Aula': {} 
} 

def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 

    priority_queue = [(0, start)] 
     
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) 
        
        if current_distance > distances[current_node]: 
            continue 

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight 

            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 

    return distances 

hasil = dijkstra(graph, 'Gerbang') 

print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit")

'''
# Jawaban:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu tempuh 2 menit.
#    Karena dibandingkan dengan Perpustakaan (6 menit), Kantin memiliki jarak paling kecil.
#
# 2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
#    Jalur tercepat: Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7 menit.
#    Meskipun ada jalur langsung Gerbang -> Kantin -> Aula = 2 + 7 = 9 menit,
#    tetapi jalur melalui Lab lebih cepat.
#
# 3. Tidak, jalur langsung tidak selalu menghasilkan jarak paling kecil.
#    Hal ini karena bisa saja ada jalur lain yang lebih panjang (lebih banyak titik),
#    tetapi memiliki total bobot (waktu) yang lebih kecil.
#    Contohnya pada kasus ini, jalur lewat Lab lebih cepat daripada jalur langsung ke Aula.
#
# 4. Dijkstra cocok digunakan pada kasus ini karena:
#    1) Semua bobot bernilai positif (waktu tempuh tidak mungkin negatif).
#    2) Ingin mencari jalur tercepat dari satu titik ke semua lokasi lain.
#    3) Algoritma ini efisien dan akurat untuk menentukan rute terbaik dalam peta lokasi seperti kampus.
'''