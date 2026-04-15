# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# ==============================================

# ==============================================
# Latihan 3 : Mmebuat Traversal Pre-order
# ==============================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data           # menyimpan nilai node
        self.left = None           # child kiri
        self.right = None          # child kanan

# Fungsi Pre-order : Root => Left => Right
def preorder(node):
    if node is not None:            # jika node kosong
        print(node.data, end='')    # tampilkan data node saat ini
        preorder(node.left)         # kunjungi subtree kiri
        preorder(node.right)        # kunjungi subtree kanan

# Membuat sebuah node root
root = Node("A")

# Membuat child Level 1
root.left = Node("B")               # child kiri dari A
root.right = Node("C")              # child kanan dari A

# Membuat child Level 2
root.left.left = Node("D")          # child kiri dari B
root.left.right = Node("E")         # child kanan dari B

# Menjalankan traversal preorder
print("Hasil Traversal Preorder: ")
preorder(root)                      # panggil fungsi               

'''
# ==============================================
# Pembahasan:
# ==============================================

# Pada kode ini, kita mempelajari traversal tree menggunakan metode Pre-order, 
# yaitu dengan urutan Root, kemudian Left, lalu Right. Pertama dibuat class Node sebagai dasar pembentukan tree, 
# yang memiliki data serta child kiri dan kanan. Setelah itu dibuat fungsi preorder yang menggunakan konsep rekursif, 
# di mana fungsi akan terus memanggil dirinya sendiri untuk menelusuri setiap node. Jika node tidak kosong, 
# maka data node tersebut akan langsung ditampilkan, kemudian fungsi akan melanjutkan ke child kiri dan setelah itu ke child kanan. 
# Selanjutnya dibuat struktur tree dengan root "A", yang memiliki child "B" di kiri dan "C" di kanan, 
# lalu "B" memiliki dua child yaitu "D" dan "E". Saat fungsi preorder dijalankan mulai dari root, 
# urutan yang dihasilkan adalah A, B, D, E, C sesuai dengan aturan Root-Left-Right. 
# Kode ini menunjukkan bagaimana traversal digunakan untuk mengunjungi semua node dalam tree secara terstruktur.
'''
