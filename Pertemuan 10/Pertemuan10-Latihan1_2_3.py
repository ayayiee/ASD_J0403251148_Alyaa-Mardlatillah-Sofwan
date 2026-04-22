# =====================================
# Nama: Alyaa Madlatillah Sofwan
# NIM: J0403251148
# Kelas : TPL B-1 
# ======================================


# ======================================
# Latihan 1 : BST
# ======================================

class Node:
    def __init__(self, data):
        self.data = data        # nilai pada node
        self.left = None        # child kiri
        self.right = None       # child kanan

def insert(root, data):
    # Jika tree kosong, buat node baru sebagai root
    if root is None:
        return Node(data)
    
    # Jika data < root, masuk ke subtree kiri
    if data < root.data:       
        root.left = insert(root.left, data)

     # Jika data > root, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

# Mengisi data BST
root = None
data_list = [50, 30, 70, 40, 50, 80]

for data in data_list:
    root = insert (root, data)

print("BST berhasil dibuat")

# ===================================
# Latihan 2 : Traversal Inorder
# ===================================

def inorder(root):
    if root is not None:                # jika node kosong
        inorder(root.left)              # kunjungi subtree kiri
        print(root.data, end=" ")       # tampilkan data node
        inorder(root.right)             # kunjungi subtree kanan

print("Hasil Inorder: ")
inorder(root)                           # panggil fungsi inorder

# =====================================
# Latihan 3 : Search di BST
# =====================================

def search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True
    elif key < root.data:
        return search(root.left, key)
    else: 
        return search(root.right, key)
    
# Uji Pencarian
key = 10

if search(root, key):                   # jika fungsi search mengembalikan True
    print("Data Ditemukan")
else: 
    print("Data Tidak Ditemukan")


'''
# ===========
# Penjelasan
# ===========

# Latihan 1
Pada bagian ini, program bertujuan untuk membangun struktur Binary Search Tree (BST). 
Proses dimulai dengan membuat class Node yang berfungsi sebagai elemen dasar tree, 
di mana setiap node menyimpan satu data serta memiliki dua cabang yaitu kiri dan kanan. 
Selanjutnya, fungsi insert digunakan untuk memasukkan data ke dalam BST secara rekursif. 
Jika tree masih kosong, maka data pertama akan menjadi root. Untuk data berikutnya, 
program akan membandingkan nilai data dengan node saat ini: jika lebih kecil akan dimasukkan ke subtree kiri, 
dan jika lebih besar ke subtree kanan. Proses ini berlangsung terus hingga posisi yang tepat ditemukan. 
Dengan menggunakan perulangan, setiap data dalam data_list dimasukkan satu per satu sehingga terbentuk struktur BST. 
Jika terdapat data yang sama, maka tidak dimasukkan karena tidak memenuhi kondisi < atau >.

# Latihan 2
Pada bagian ini, program menampilkan isi BST menggunakan metode traversal inorder. 
Fungsi inorder bekerja secara rekursif dengan mengunjungi subtree kiri terlebih dahulu, 
kemudian menampilkan data pada node saat ini, dan terakhir mengunjungi subtree kanan. 
Karena sifat BST yang menempatkan nilai lebih kecil di kiri dan lebih besar di kanan, 
traversal inorder akan menghasilkan data dalam urutan yang terurut dari kecil ke besar. 
Fungsi ini dipanggil setelah BST selesai dibuat, sehingga hasil yang ditampilkan mencerminkan isi tree secara sistematis.

# Latihan 3
Pada bagian ini, program melakukan pencarian suatu nilai dalam BST menggunakan fungsi search. 
Proses dimulai dari root, kemudian membandingkan nilai yang dicari (key) dengan data pada node saat ini. 
Jika sama, maka pencarian berhasil dan fungsi mengembalikan nilai True. Jika nilai yang dicari lebih kecil, 
maka pencarian dilanjutkan ke subtree kiri, sedangkan jika lebih besar akan dilanjutkan ke subtree kanan. 
Proses ini dilakukan secara rekursif hingga data ditemukan atau mencapai node kosong (yang berarti data tidak ada dalam tree). 
Hasil pencarian kemudian ditampilkan dalam bentuk pesan apakah data ditemukan atau tidak.
'''