# ========================================
# Nama : Alyaa Mardlatillah Sofwan
# NIM : J0403251148
# Kelas : TPL B-1
# latihan 3 : Implementasi Algoritma Prim
# ========================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):
    visited = set([start])
    edges = []
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))
    mst = []
    total_weight = 0
    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            total_weight += weight
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)

'''
Jawaban: 
1. Node awal apa yang digunakan? 
Node 'A'

2. Edge mana yang dipilih pertama kali? 
Edge antara node A dan C dengan bobot 2, karena memiliki bobot paling kecil di antara semua edge
yang terhubung langsung dengan node A.

3. Bagaimana Prim menentukan edge berikutnya? 
Dengan cara memilih edge berbobot paling kecil yang menghubungkan node yang sudah dikunjungi ke node
yang belum dikunjungi. Dengan ini, graph dapat terus berkembang tanpa membentuk cycle.

4. Berapa total bobot MST yang dihasilkan? 
Total bobotnya adalah 6 (A ke C = 2, C ke D = 1, D ke B = 3).

5. Apa perbedaan pendekatan Prim dan Kruskal? 
Kalau prim dimulai dari satu titik, lalu ke titik terdekat yang paling kecil bobotnya sampai semua terhubung.
kalau kruskal mengurutkan semua edge dari yang terkecil, lalu diambil satu persatu selama tidak membentuk cycle.
'''

