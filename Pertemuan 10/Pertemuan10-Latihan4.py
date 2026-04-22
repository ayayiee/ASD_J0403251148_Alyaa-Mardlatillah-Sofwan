# =====================================
# Nama: Alyaa Madlatillah Sofwan
# NIM: J0403251148
# Kelas : TPL B-1 
# ======================================


# ===========================================
# Latihan 4 : Membuat BST yang Tidak Seimbang
# ===========================================

# Class node yang menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data        # nilai pada node
        self.left = None        # child kiri
        self.right = None       # child kanan

# Fungsi insert untuk BST
def insert (root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)

    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)

    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    return root                                         # mengembalikan root yang sudah diperbarui

# Fungsi preorder untuk melihat bentuk tree 
def preorder (root):
    if root is not None:                                # jiika node tidak kosong
        print(root.data, end=" ")                       # tampilkan data node
        preorder(root.left)                             # telusuri subtree kiri
        preorder(root.right)                            # telusuri subtree kanan

# Fungsi sederhana untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")  # tampilkan node dengan indentasi sesuai level
        tampil_struktur(root.left, level + 1, "L")      # tampilkan subtree kiri dengan level lebih dalam
        tampil_struktur(root.right, level + 1, "R")     # tampilkan subtree kanan dengan level lebih dalam

# ------------------------
# Program Utama
# ------------------------
root = None

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST: ")
preorder(root)                                            #  tampilkan isi BST dengan traversal preorder

print("\n\nStruktur BST: ")
tampil_struktur(root)                                     # Tampilkan struktur BST secara visual sederhana

'''
# ===========
# Penjelasan 
# ===========

Pada bagian ini dilakukan pembuatan Binary Search Tree (BST) dengan kondisi tidak seimbang (unbalanced) 
menggunakan kelas 'Node' yang memiliki atribut 'data', 'left', dan 'right untuk merepresentasikan setiap elemen dalam tree. 
Proses pembentukan BST dilakukan melalui fungsi 'insert' secara rekursif, di mana jika node masih kosong maka akan dibuat node baru, 
sedangkan jika tidak kosong maka data akan dibandingkan dengan nilai pada node saat ini untuk menentukan posisi penyisipan, 
yaitu ke subtree kiri jika lebih kecil dan ke subtree kanan jika lebih besar. Data dimasukkan secara berurutan dalam kondisi menaik, 
yaitu '[10, 20, 30]', sehingga setiap data baru selalu ditempatkan di sisi kanan node sebelumnya. 
Hal ini menyebabkan struktur tree menjadi tidak seimbang dan cenderung menyerupai linked list. Untuk menampilkan isi tree, 
digunakan fungsi 'preorder' yang melakukan traversal dengan urutan node, subtree kiri, kemudian subtree kanan, 
serta fungsi 'tampil_struktur' yang menampilkan struktur tree secara sederhana menggunakan indentasi berdasarkan level kedalaman 
node dan penanda posisi (Root, L, R), sehingga bentuk ketidakseimbangan BST dapat terlihat dengan jelas.
'''