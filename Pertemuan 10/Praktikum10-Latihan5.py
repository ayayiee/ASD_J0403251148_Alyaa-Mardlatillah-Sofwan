# =====================================
# Nama: Alyaa Madlatillah Sofwan
# NIM: J0403251148
# Kelas : TPL B-1 
# ======================================


# ===============================================
# Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang
# ===============================================

# Class node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Fungsi rotasi kiri 
def rotate_left(x):
    # x adalah root lama
    y = x.right # y adalah child kanan x
    T2 = y.left # subtree krii milik y disimpan sementara

    # Proses rotasi
    y.left = x # x menjadi child krii dari y
    x.right = T2 # child kanan  x diganti dengan T2

    # y menjadi root baru
    return y

# --------------------------
# program utama
# --------------------------

# Mmebuat tree yang tidak seimbang:
# 10 -> 20 -> 30
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebellum rotasi kiri: ")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri: ")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri: ")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri: ")
tampil_struktur(root)

'''
# ==========
# Penjelasan
# ==========

Pada bagian ini dilakukan proses rotasi kiri (left rotation) pada Binary Search Tree (BST) yang tidak seimbang. 
Awalnya, tree dibentuk secara manual dengan struktur condong ke kanan, yaitu node 10 sebagai root, 
diikuti node 20 sebagai anak kanan, dan node 30 sebagai anak kanan dari node 20. Struktur ini menunjukkan kondisi 
tidak seimbang karena semua node berada pada satu sisi. Untuk mengatasi hal tersebut, digunakan fungsi rotate_left yang 
bertujuan menyeimbangkan struktur tree. Proses rotasi dimulai dengan menjadikan child kanan dari root (node 20) sebagai root baru, 
sementara node 10 dipindahkan menjadi child kiri dari node 20. Subtree kiri dari node 20 (jika ada) disimpan sementara dan kemudian 
dijadikan child kanan dari node 10. Setelah rotasi dilakukan, struktur tree menjadi lebih seimbang dengan node 20 sebagai root, 
 10 sebagai anak kiri, dan node 30 sebagai anak kanan. Perubahan ini ditampilkan menggunakan traversal preorder serta fungsi tampil_struktur, 
 sehingga perbedaan struktur sebelum dan sesudah rotasi dapat diamati dengan jelas.
 
'''