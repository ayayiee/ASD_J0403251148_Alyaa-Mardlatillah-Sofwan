# ==========================================
# Nama : Alyaa Mardlatillah SOfwan
# NIM: J0403251148
# Kleas : TPL B-1
# Implementasi DFS
# ==========================================

# struktur data untuk membuat antrian, kita gunakan dari library collections bawaan python
from collections import deque


# Representasi graph
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}

def dfs (graph, node, visited):
    # fungsi untuk melakukan penuusuran graph dengan dfs
    # graph : dictionary yang menyimpan struktur graph
    # node : menyimpan node yang sedang dikunjungi
    # visited : menyimpan node yang sudah dikunjungi

    # tandai node saat ini sebagai node yang sudha dikunjungi
    visited.add(node)

    # tampilkan node
    print(node, end=" ")

    # periksa semua tetangga dari node saat ini 
    for neighbor in graph[node]:

        # jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            # lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

# set visited
visited = set()

# Menjalankan dfs dari A
dfs(graph, 'A', visited)

