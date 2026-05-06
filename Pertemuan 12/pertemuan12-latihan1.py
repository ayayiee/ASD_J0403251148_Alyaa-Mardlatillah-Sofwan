# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# Praktikum 12 - Graph II: Shortest Path
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ===============================================

# Representasi weighted graph menggunakan dictionary bersarang 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 

# Menghitung dua kemungkinan jalur dari A ke D 
jalur_1 = graph['A']['B'] + graph['B']['D']   # A -> B -> D 
jalur_2 = graph['A']['C'] + graph['C']['D']   # A -> C -> D

print("Jalur 1: A -> B -> D =", jalur_1) 
print("Jalur 2: A -> C -> D =", jalur_2) 

if jalur_1 < jalur_2: 
    print("Jalur terpendek adalah A -> B -> D") 
else: 
    print("Jalur terpendek adalah A -> C -> D")

'''
# Jawaban:
# 1. Total bobot jalur adalah 9 (A -> B -> D = 4 + 5 = 9)
#
# 2. Total bobot jalur adalh 3 (A -> C -> D = 2 + 1 = 3)
#
# 3. Jalur terpendek adalah A -> C -> D karena memiliki total bobot lebih kecil (3 < 9)
#
# 4. Jalur terpendek tidak selalu ditentukan dari jumlah edge paling sedikit karena setiap edge memiliki bobot (nilai) yang berbeda.
#    Jalur dengan edge lebih sedikit bisa saja memiliki bobot total lebih besar dibanding jalur dengan edge lebih banyak.
#    Oleh karena itu, yang menentukan jalur terpendek adalah total bobot, bukan jumlah edge.
'''