# ========================================
# Nama : Alyaa Mardlatillah Sofwan
# NIM : J0403251148
# Kelas : TPL B-1
# latihan 4 : Jaringan Kabel Antara Gedung
# ========================================

import heapq

# Representasi weighted graph
graph = {
    'Gedung A': {'Gedung B': 4, 'Gedung C': 2, 'Gedung D': 5},
    'Gedung B': {'Gedung A': 4, 'Gedung D': 3},
    'Gedung C': {'Gedung A': 2, 'Gedung D': 1},
    'Gedung D': {'Gedung A': 5, 'Gedung B': 3, 'Gedung C': 1}
}


def prim(graph, start):
    visited = set([start]) # Menyimpan node yang sudah dikunjungi
    edges = []             # Menyimpan edge yang akan diproses

    # Memasukkan semua edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():           
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total biaya
    total_weight = 0

    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan total bobot
            total_weight += weight

            # Memasukkan edge baru dari node yang dipilih
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight

# Memanggil fungsi Prim dimulai dari GedungA
mst, total = prim(graph, 'GedungA')
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total)

'''
Jawaban: 
1. Algoritma apa yang digunakan? 
Algoritma yang digunakan adalah algoritma Prim.

2. Edge mana saja yang dipilih? 
Gedung A - Gedung C dengan bobot 2
Gedung C - Gedung D dengan bobot 1
Gedung D - Gedung B dengan bobot 3

3. Berapa total biaya minimum? 
Total biaya minimum yang dihasilkan adalah 6 (2 + 1 + 3 = 6 -> penjumlahan 
seluruh bobot edge)

4. Mengapa MST cocok digunakan pada kasus ini?
MST cocok digunakan pada kasus ini karena tujuan pembangunan jaringan kabel 
antar gedung adalah menghubungkan seluruh gedung dengan biaya seminimum mungkin. 
Dengan menggunakan MST, semua gedung dapat tetap terhubung tanpa perlu menambahkan 
jalur yang tidak diperlukan sehingga biaya pemasangan kabel menjadi lebih efisien.
'''