# ==========================================
# Nama : Alyaa Mardlatillah SOfwan
# NIM: J0403251148
# Kleas : TPL B-1
# Implementasi BFS
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

def bfs (graph, start):
    # fungsi untuk melakukan penuusuran graph dengan bfs
    # graph : dictionary yang menyimpan struktur graph
    # start : node awal penulusuran

    # Queue digunakan untuk menyimpan node yang akan diproses/dibaca
    queue = deque()

    # variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
    visited = set ()

    # Masukkan node awal ke queue
    queue.append(start)

    # tandai node awal sebagai nodeyang sudah dkunjungi
    visited.add(start)

    while queue:
        # mengambil node paling depan dari queue
        node = queue.popleft() 

        # Tampilkan node yang sedang dikunjungi
        print(node, end=" ")
        # periksa smeua tetangga nya yang diambil 
        for neighbor in graph [node]:
            # jika tetangga belum dikunjungi
            if neighbor not in visited: 
                if neighbor not in visited:
                    # tandai sebagai sudah dikunjungi
                    visited.add(neighbor)
                    # masukkan tetangga ke queue untuk diproses nanti
                    queue.append(neighbor)

# menjalankan BSF dari node A
bfs(graph, 'A')
