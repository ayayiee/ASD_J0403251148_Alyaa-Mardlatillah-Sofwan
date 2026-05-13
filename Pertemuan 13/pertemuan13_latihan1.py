# ====================================
# Nama : Alyaa Mardlatillah Sofwan
# NIM : J0403251148
# Kelas : TPL B-1
# Graph III: Spanning Tree 
# ====================================

# Daftar edge graph 
edges = [ 
  ('A', 'B'), 
  ('A', 'C'), 
  ('A', 'D'), 
  ('C', 'D'), 
  ('B', 'D') 
] 

# Contoh spanning tree 
spanning_tree = [ 
  ('A', 'C'), 
  ('C', 'D'), 
  ('D', 'B') 
] 

print("Edge pada graph:") 
for edge in edges: 
  print(edge) 
  
print("\nSpanning Tree:")
for edge in spanning_tree: 
  print(edge) 
  
print("\nJumlah edge graph =", len(edges)) 
print("Jumlah edge spanning tree =", len(spanning_tree))


#Pertanyaan Analisis 
'''
Jawaban:

1. Apa perbedaan graph awal dan spanning tree? 
graph awal menampilkan seluruh jalur yang memungkinkan serta terdapat cycle dan jumlah edge yang besar. 
sedangkan spanning tree hanya mengambil jalur yang penting agar semua node tetap terhubung tanpa
membentuk cycle.

2. Mengapa spanning tree tidak boleh memiliki cycle? 
karena tujuan utamanya adalah membentuk hubungan yang sederhana dan terhubung secara efisien.
Jika terdapat cycle, maka akan ada jalur yang berulang sehingga beberapa edge menjadi tidak diperlukan.

3. Mengapa jumlah edge spanning tree selalu lebih sedikit? 
karena spanning tree dibuat seefisien mungkin dengan hanya mengambil jalur yang diperlukan untuk menghubungkan
semua titik. Oleh sebab itu, tidak digunakan edge tambahan yang dapat membentuk jalur berulang.
Jika sebuah graph memiliki 4 titik, makan spanning tree cukup membutuhkan 3 edge
agar seluruh titik dapat saling terhubung.
'''