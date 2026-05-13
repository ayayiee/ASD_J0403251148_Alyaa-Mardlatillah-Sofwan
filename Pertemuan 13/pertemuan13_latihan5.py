# ========================================
# Nama : Alyaa Mardlatillah Sofwan
# NIM : J0403251148
# Kelas : TPL B-1
# latihan 5 : Buat Program MST dengan Kasus Baru
# ========================================

edges = [
    (3, 'Router A', 'Router B'),
    (2, 'Router A', 'Router C'),
    (5, 'Router B', 'Router D'),
    (1, 'Router C', 'Router D'),
    (4, 'Router B', 'Router C')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Struktur untuk mengecek cycle (Union-Find sederhana)
parent = {}

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(a, b):
    parent[find(a)] = find(b)

# Inisialisasi parent
nodes = ['RouterA', 'RouterB', 'RouterC', 'RouterD']
for n in nodes:
    parent[n] = n

mst = []
total_weight = 0

# Kruskal Algorithm
for weight, u, v in edges:
    if find(u) != find(v):  # tidak membentuk cycle
        union(u, v)
        mst.append((u, v, weight))
        total_weight += weight

# Output hasil MST
print("Minimum Spanning Tree:")
for u, v, w in mst:
    print((u, v, w))

print("Total bobot minimum =", total_weight)

'''
Jawaban:
1. Kasus apa yang dipilih? 
Kasus yang dipilih adalah kasus 2.

2. Algoritma apa yang digunakan? 
Algoritma yang digunakan adalah Kruskal.

3. Edge mana saja yang dipilih dalam MST? 
Router C - Router D dengan bobot 1
Router A - Router C dengan bobot 2
Router A - Router B dengan bobot 3

4. Berapa total bobot MST? 
Total bobot MST adalah 6 (1 + 2 + 3 = 6)

5. Mengapa edge tertentu tidak dipilih? 
Karena jika edge tersebut ditambahkan, akan membentuk cycle atau
memiliki bobot lebih besar sehingga tidak efisien. 
MST hanya memilih jalur minimum agar semua node tetap terhubung tanpa 
kelebihan koneksi.
'''