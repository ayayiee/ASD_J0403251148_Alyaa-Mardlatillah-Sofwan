# ====================================
# Nama : Alyaa Mardlatillah Sofwan
# NIM : J0403251148
# Kelas : TPL B-1
# Implementasi Prim
# ====================================

import heapq 
 
graph = {                           # Membuat representasi graph 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 
 
def prim(graph, start):             # Fungsi algoritma Prim dengan parameter graph dan node awal
 
    visited = set([start])          # Menyimpan node yang sudah dikunjungi, dimulai dari node start
 
    edges = []                      # List untuk menyimpan edge yang akan diproses
 
    for neighbor, weight in graph[start].items():            # Mengambil semua neighbor dari node awal
        heapq.heappush(edges, (weight, start, neighbor))     # Memasukkan edge ke priority queue berdasarkan bobot terkecil
 
    mst = []                        # Menyimpan hasil Minimum Spanning Tree
    total_weight = 0 
 
    while edges:                    # Selama masih ada edge di priority queue
 
        weight, u, v = heapq.heappop(edges)                   # Mengambil edge dengan bobot paling kecil
 
        if v not in visited:                                  # Jika node tujuan belum dikunjungi
 
            visited.add(v)                                    # Menandai node sebagai sudah dikunjungi     
 
            mst.append((u, v, weight))                        # Menambahkan edge ke MST
            total_weight += weight                            # Menambahkan bobot edge ke total bobot
 
            for neighbor, w in graph[v].items():              # Mengecek semua neighbor dari node v
 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor))   # Menambahkan edge baru ke priority queue
 
    return mst, total_weight


mst, total = prim(graph, 'A')         # Memanggil fungsi prim mulai dari node A
 
print("Minimum Spanning Tree:") 
 
for edge in mst:                      # Loop untuk menampilkan setiap edge MST
    print(edge) 
 
print("Total bobot =", total)