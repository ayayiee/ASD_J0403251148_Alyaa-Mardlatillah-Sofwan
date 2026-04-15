# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# ==============================================

# ==============================================
# Latihan 6 : Struktur Organisasi Perusahaan
# ==============================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data               # menyimpan nilai node
        self.left = None               # child kiri
        self.right = None              # child kanan

# Fungsi Pre-order : Root => Left => Right
def preorder(node):
    if node is not None:
        print(node.data, end='')       # tampilkan data node
        preorder(node.left)            # kunjungi child kiri
        preorder(node.right)           # kunjungi child kanan

# Membuat tree struktur organisasi
root = Node("Direktur")                # node paling atas 

# Membuat child Level 1
root.left = Node("Manajer A")          # bawahan kiri direktur
root.right = Node("Manajer B")         # bawahan kanan direktur

# Membuat child Level 2
root.left.left = Node("Staff1")        # staff di bawah manajer A
root.left.right = Node("Staff2")       # staff di bawah manajer A

root.right.right = Node("Staff3")      # staff di bawah manajer B

# menjalankan traversal 
print("Struktur Organisasi (preorder): ")
preorder(root)                         # menampilkan struktur organisai

'''
# ==============================================
# Pembahasan:
# ==============================================

# Pada kode ini, struktur tree digunakan untuk merepresentasikan struktur organisasi perusahaan. 
# Setiap node mewakili jabatan, dimulai dari root sebagai "Direktur" yang merupakan posisi tertinggi. 
# Kemudian terdapat dua child yaitu "Manajer A" dan "Manajer B" sebagai bawahan langsung dari direktur. 
# Selanjutnya, "Manajer A" memiliki dua staff yaitu "Staff1" dan "Staff2", sedangkan "Manajer B" memiliki satu staff yaitu "Staff3". 
# Untuk menampilkan struktur organisasi, digunakan traversal Preorder yang mengikuti urutan Root, Left, dan Right, 
# sehingga data ditampilkan mulai dari direktur, kemudian ke bagian kiri (Manajer A beserta staffnya), 
# lalu ke bagian kanan (Manajer B dan staffnya). Pendekatan ini cocok digunakan untuk menggambarkan hierarki organisasi 
# karena menampilkan atasan terlebih dahulu sebelum bawahannya.
'''