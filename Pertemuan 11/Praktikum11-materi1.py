# ==========================================
# Nama : Alyaa Mardlatillah SOfwan
# NIM: J0403251148
# Kleas : TPL B-1
# Implementasi dasar Graph
# ==========================================

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D'],
    'C' : ['A', 'D'],
    'D' : ['B', 'C']
}

for node in graph:
    print(node, "->", graph[node])