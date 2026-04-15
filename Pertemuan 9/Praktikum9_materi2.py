# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# ==============================================

# ==============================================
# Latihan 2 : Membuat Binary Search Tree Sederhana
# ==============================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data       # menyimpan nilai node
        self.left = None       # pointer ke child kiri
        self.right = None      # pointer ke child kanan

# Membuat sebuah node root
root = Node("A")

# Membuat child Level 1
root.left = Node("B")          # node B menjadi child kiri dari A
root.right = Node("C")         # node C menjadi child kanan dari A

# Membuat child Level 2
root.left.left = Node("D")     # node D menjadi child kiri dari B
root.left.right = Node("E")    # node E menjadi child kanan dari B

#membuat child level 3
root.right.left = Node("F")    # node F menjadi child kiri dari C
root.right.right = Node("G")   # node G menjadi child kanan dari C

# Menampilkan isi kode

#menampilkan isi node
print("Data pada root", root.data)                      # menapilkan data root (A)
print("Child kiri root", root.left.data)                # menampilkan child kiri root (B)
print("Child kanan root", root.right.data)              # menampilkan child kanan root (C)
print("Child kiri dari B: ", root.left.left.data)       # menampilkan child kiri root (D)
print("Child kanan dari B: ", root.left.right.data)     # menampilkan child kanan root (E)
print("Child kiri dari C: ", root.right.left.data)      # menampilkan child kiri root (F)
print("Child kanan dari C: ", root.right.right.data)    # menampilkan child kanan root (G)

'''
# ==============================================
# Pembahasan:
# ==============================================

# Pada kode ini, kita membangun struktur tree secara manual menggunakan class Node, 
# di mana setiap node memiliki data serta dua child yaitu left dan right. Pertama dibuat root dengan nilai "A" sebagai node utama. 
# Kemudian ditambahkan child level 1 yaitu "B" sebagai child kiri dan "C" sebagai child kanan dari root. 
# Selanjutnya, node "B" memiliki dua anak yaitu "D" di kiri dan "E" di kanan, yang disebut sebagai level 2. 
# Lalu node "C" juga memiliki dua anak yaitu "F" di kiri dan "G" di kanan, yang membentuk level berikutnya. 
# Dengan demikian, terbentuk struktur tree bercabang dengan beberapa level. 
# Pada bagian akhir, program menampilkan isi dari setiap node dengan mengakses atribut data melalui relasi 
# parent-child (misalnya root.left.right untuk mengambil node E). Kode ini menunjukkan bagaimana struktur tree 
# dapat dibangun secara bertingkat dan bagaimana cara mengakses setiap node di dalamnya.
'''