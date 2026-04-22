# =====================================
# Nama: Alyaa Madlatillah Sofwan
# NIM: J0403251148
# Kelas : TPL B-1 
# ======================================

# ===============================================
# Latihan 6 : Rotasi Kiri pada BST Tidak Seimbang
# ===============================================

# Class node
class Node:
    def __init__(self, data):
        self.data = data        # menyimpan nilai node
        self.left = None        # pointer ke child kiri
        self.right = None       # pointer ke child kanan

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:        # jika node tidak kosong
        print(root.data, end=" ")  # tampilkan data
        preorder(root.left)        # ke subtree kiri
        preorder(root.right)       # ke subtree kanan

# Fungsi menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")  # tampilkan node + indentasi
        tampil_struktur(root.left, level + 1, "L")      # subtree kiri
        tampil_struktur(root.right, level + 1, "R")     # subtree kanan

# Fungsi rotasi kanan
def rotate_right(y):
    x = y.left               # x adalah child kiri dari y (akan jadi root baru)
    T2 = x.right             # subtree kanan milik x disimpan sementara

    # Proses rotasi kanan
    x.right = y              # y menjadi child kanan dari x
    y.left = T2              # subtree kiri y diganti dengan T2

    return x                 # kembalikan root baru

# --------------------------
# Program Utama
# --------------------------

# Membuat tree tidak seimbang (condong ke kiri):
# 30 -> 20 -> 10
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Preorder sebelum rotasi kanan: ")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan: ")
tampil_struktur(root)

# Rotasi kanan pada root
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan: ")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan: ")
tampil_struktur(root)

'''
# ===========
# Penjelasan
# ===========

# Pada bagian ini dilakukan proses rotasi kanan (right rotation) pada Binary Search Tree (BST) yang tidak seimbang. 
# Awalnya, tree dibentuk dalam kondisi condong ke kiri dengan struktur node 30 sebagai root, node 20 sebagai anak kiri, 
# dan node 10 sebagai anak kiri dari node 20. Struktur ini menunjukkan ketidakseimbangan karena seluruh node berada pada satu sisi. 
# Untuk memperbaiki struktur tersebut, digunakan fungsi rotate_right yang bekerja dengan menjadikan child kiri dari root sebagai root baru. 
# Dalam proses ini, node 20 menjadi root baru, sementara node 30 dipindahkan menjadi child kanan dari node 20. 
# Subtree kanan dari node 20 (jika ada) disimpan sementara dan kemudian dipindahkan sebagai child kiri dari node 30. 
# Setelah rotasi dilakukan, struktur tree menjadi lebih seimbang dengan node 20 sebagai root, node 10 sebagai anak kiri, 
# dan node 30 sebagai anak kanan. Hasil perubahan ini ditampilkan menggunakan traversal preorder serta fungsi tampil_struktur 
# sehingga perbedaan struktur sebelum dan sesudah rotasi dapat diamati dengan jelas.
'''