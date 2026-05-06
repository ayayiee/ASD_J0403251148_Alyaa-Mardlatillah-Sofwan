# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 3: Implementasi Bellman-Ford 
# ===============================================

# Weighted graph dengan bobot negatif 
graph = { 
    'A': {'B': 5, 'C': 4}, 
    'B': {}, 
    'C': {'B': -2} 
} 
 
def bellman_ford(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Bellman-Ford. 
    """ 
 
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
 
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
 
    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1 
    for _ in range(len(graph) - 1): 
 
        # Periksa semua edge 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
 
                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak 
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    return distances 
 
hasil = bellman_ford(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)

'''
# Jawaban:
# 1. Bobot langsung dari A ke B = 5
#    Karena terdapat edge langsung dari A ke B dengan nilai bobot 5.
#
# 2. Total bobot jalur A -> C -> B = 4 + (-2) = 2
#    Dari A ke C bobotnya 4, lalu dari C ke B bobotnya -2, sehingga totalnya 2.
#
# 3. Jalur yang menghasilkan jarak lebih kecil menuju B adalah A -> C -> B
#    Karena total bobotnya 2, lebih kecil dibanding jalur langsung A -> B yang bernilai 5.
#
# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena algoritma ini
#    tidak langsung menetapkan jarak sebagai final. Ia melakukan perulangan (relaksasi)
#    berkali-kali sehingga bisa menemukan kemungkinan jalur yang lebih pendek,
#    termasuk yang melibatkan bobot negatif.
#
# 5. Relaksasi edge adalah proses membandingkan jarak lama dengan jarak baru yang mungkin lebih kecil.
#    Jika ditemukan jalur yang lebih pendek (misalnya lewat node lain), maka jarak akan diperbarui.
#    Contohnya: jika A -> B awalnya 5, lalu ditemukan jalur A -> C -> B = 2, maka nilai B di-update jadi 2.
#
# 6. Perbedaan utama Bellman-Ford dan Dijkstra:
#    - Bellman-Ford bisa menangani bobot negatif, sedangkan Dijkstra tidak bisa.
#    - Dijkstra lebih cepat (efisien) karena menggunakan priority queue (greedy).
#    - Bellman-Ford lebih lambat karena memeriksa semua edge berulang kali.
#    - Bellman-Ford juga bisa mendeteksi negative cycle, sedangkan Dijkstra tidak.
'''