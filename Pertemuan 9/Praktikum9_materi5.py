# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# ==============================================

# ==============================================
# Latihan 5 : Membuat Traversal post Order
# ==============================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data            # menyimpan nilai node
        self.left = None            # child kiri
        self.right = None           # child kanan

# Membuat fungsi Post Order; left => root => right
def postorder(node):
    if node is not None:
        postorder(node.left)        # kunjungi subtree kiri
        postorder(node.right)       # kunjungi subtree kiri
        print(node.data, end=" ")   # tampilkan data node terakhir

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
postorder(root)                     # emmanggil fungsi 

'''
# ==============================================
# Pembahasan:
# ==============================================

# Pada kode ini, kita mempelajari traversal tree menggunakan metode Postorder, 
# yaitu dengan urutan Left, kemudian Right, lalu Root. Pertama dibuat class Node sebagai dasar 
# pembentukan tree yang memiliki data serta child kiri dan kanan. Selanjutnya dibuat fungsi postorder yang menggunakan 
# rekursi untuk menelusuri tree. Fungsi ini akan terlebih dahulu mengunjungi subtree kiri, kemudian subtree kanan, dan 
# terakhir menampilkan data node saat ini. Setelah itu dibentuk struktur tree dengan root "A", yang memiliki child "B" 
# di kiri dan "C" di kanan, serta node "B" memiliki dua child yaitu "D" dan "E". Saat fungsi postorder dijalankan dari root, 
# urutan yang dihasilkan adalah D, E, B, C, A sesuai dengan aturan Left-Right-Root. Traversal ini biasanya digunakan ketika 
# kita ingin memproses child terlebih dahulu sebelum parent, misalnya pada penghapusan node dalam tree.
'''