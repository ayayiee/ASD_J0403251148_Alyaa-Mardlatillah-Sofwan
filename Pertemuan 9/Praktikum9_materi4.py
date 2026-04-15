# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# ==============================================

# ==============================================
# Latihan 4 : Membuat Traversal Inorder
# ==============================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data           # menyimpan nilai node
        self.left = None           # child kiri
        self.right = None          # child kanan

# Membuat fungsi inorder ; left => root => right
def inorder(node):
    if node is not None:
        inorder(node.left)          # kunjungi subtree kiri terlebih dahulu
        print(node.data, end=" ")   # tampilkan data node
        inorder(node.right)         # kunjungi subtree kanan

# Membuat sebuah node root
root = Node("A")

# Membuat child Level 1
root.left = Node("B")               # child kiri dari A
root.right = Node("C")              # child kanan dari A

# Membuat child Level 2
root.left.left = Node("D")          # child kiri dari B
root.left.right = Node("E")         # child kanan dari B

# Menjalankan traversal preorder
print("Hasil Traversal Inorder: ")
inorder(root)                       # memanggil fungsi

'''
# ==============================================
# Pembahasan:
# ==============================================

# Pada kode ini, kita mempelajari traversal tree menggunakan metode Inorder, yaitu dengan urutan Left, kemudian Root, lalu Right. 
# Pertama dibuat class Node sebagai dasar pembentukan tree yang memiliki data serta child kiri dan kanan. 
# Selanjutnya dibuat fungsi inorder yang menggunakan rekursi untuk menelusuri tree. Fungsi ini akan terlebih dahulu mengunjungi subtree kiri, 
# kemudian menampilkan data node saat ini, dan terakhir mengunjungi subtree kanan. 
# Setelah itu dibentuk struktur tree dengan root "A", yang memiliki child "B" di kiri dan "C" di kanan, serta node "B" memiliki dua child yaitu "D" dan "E". 
# Saat fungsi inorder dijalankan dari root, urutan yang dihasilkan adalah D, B, E, A, C sesuai dengan aturan Left-Root-Right. 
# Traversal ini sering digunakan pada Binary Search Tree karena dapat menghasilkan urutan data yang terurut.
'''