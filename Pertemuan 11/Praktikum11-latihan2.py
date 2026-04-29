# ==========================================
# Nama : Alyaa Mardlatillah SOfwan
# NIM: J0403251148
# Kleas : TPL B-1
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
# ==========================================

graph = { 
    'A': ['B', 'C'],            # Node A terhubung ke B dan C   
    'B': ['D', 'E'],            # Node B terhubung ke D dan E
    'C': ['F'],                 # Node C terhubung ke F
    'D': [],                    # Node D tidak punya tetangga
    'E': [],                    # Node E tidak punya tetangga
    'F': []                     # Node F tidak punya tetangga
}

def dfs(graph, node, visited): 
    visited.add(node)           # Tandai node sebagai sudah dikunjungi
    print(node, end=" ")        # Tampilkan node

    for neighbor in graph[node]:            # Loop semua tetangga node
        if neighbor not in visited:         # Jika belum dikunjungi
            dfs(graph, neighbor, visited)   # Rekursif ke node tersebut

visited = set()                              # Set untuk menyimpan node yang sudah dikunjungi

print("DFS dari A:") 
dfs(graph, 'A', visited)                     # Mulai DFS dari node A

'''
penjelasan akur:
Kode ini menjalankan algoritma Depth First Search (DFS) pada sebuah graph yang 
direpresentasikan dalam bentuk dictionary. Proses dimulai dari node "A" yang langsung 
ditandai sebagai sudah dikunjungi dan dicetak ke layar. Setelah itu, program akan mengecek 
setiap tetangga dari node tersebut secara berurutan. Jika tetangga belum pernah dikunjungi, 
maka fungsi dfs akan dipanggil kembali (rekursif) untuk node tersebut. Proses ini membuat 
algoritma terus masuk ke node yang lebih dalam sampai mencapai node yang tidak memiliki tetangga. 
Ketika sudah mentok, program akan kembali ke node sebelumnya untuk melanjutkan ke tetangga 
lain yang belum dikunjungi. Alur ini berlangsung terus sampai semua node dalam graph telah dikunjungi.

1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
DFS (Depth First Search) menggunakan rekursi (atau stack), sehingga saat menemukan satu jalur, 
algoritma akan terus mengikuti jalur tersebut sampai mentok (node paling dalam) 
sebelum kembali (backtracking) ke node sebelumnya. 
Karena itu, DFS terlihat seperti “menyelam” ke dalam graph terlebih dahulu, bukan melebar.

2. Apa yang terjadi jika urutan neighbor diubah?
Jika urutan neighbor di dalam graph diubah, maka urutan hasil DFS juga akan berubah. 
Hal ini disebabkan karena DFS memproses tetangga sesuai dengan urutan yang diberikan 
dalam struktur data. Ketika urutan tersebut berubah, jalur yang pertama kali diikuti oleh 
DFS juga akan berubah, sehingga urutan kunjungan node menjadi berbeda meskipun graph yang digunakan tetap sama.

3. Bandingkan hasil DFS dengan BFS pada graph yang sama
DFS dan BFS memiliki perbedaan pada cara menelusuri graph. DFS menelusuri satu jalur hingga 
dalam terlebih dahulu, sedangkan BFS menelusuri secara melebar berdasarkan level. 
Pada graph yang diberikan, DFS akan menghasilkan urutan seperti A, B, D, E, C, F, 
karena dari A langsung ke B lalu masuk ke D dan E sebelum kembali ke C. Sementara itu, 
BFS akan menghasilkan urutan A, B, C, D, E, F, karena setelah mengunjungi A, 
algoritma langsung mengunjungi semua tetangga terdekatnya yaitu B dan C, 
baru kemudian ke level berikutnya yaitu D, E, dan F. Perbedaan ini menunjukkan bahwa 
BFS lebih terstruktur berdasarkan jarak, sedangkan DFS lebih fokus pada kedalaman jalur.

'''