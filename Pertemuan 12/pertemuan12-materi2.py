# =======================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# Materi 2
# =======================================

# Representasi graph sesuai gambar
graph = {
    'A': {'B': 5, 'C': 4},   
    'B': {},                 
    'C': {'B': -2}           
}

def bellman_ford(graph, start): 
    distances = {node: float('inf') for node in graph}   # Set semua jarak awal = tak hingga
    distances[start] = 0                                 
 
    # Relaksasi berulang
    for _ in range(len(graph) - 1):                      # Dilakukan sebanyak (jumlah node - 1)
        for node in graph:                               
            for neighbor, weight in graph[node].items(): # Loop semua edge (node → neighbor)
                
                # Jika ditemukan jarak lebih kecil
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight   # Update jarak lebih pendek
 
    return distances                                    

start_node = 'A'                                         # Tentukan node awal

hasil = bellman_ford(graph, start_node)                  

print("Jarak terpendek dari A:")                         
for node, jarak in hasil.items():                       
    print(f"A -> {node} = {jarak}")                      # Tampilkan jarak ke tiap node