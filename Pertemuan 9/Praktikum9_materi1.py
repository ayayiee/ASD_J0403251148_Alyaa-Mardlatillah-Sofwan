# ==============================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
# ==============================================

# ==============================================
# Latihan 1 : Membuat Node
# ==============================================

# class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data                        # menyimpan nilai node
        self.left = None                        # pointer ke child kiri
        self.right = None                       # ponter ke child kanan

# Membuat root (node utama/paling atas dalam tree)
root = Node("A")

# Menampilkan isi kode
print("Data pada root:", root.data)             # menampilkan data pada node root
print("Data child kiri: ", root.left)           # menampilkan child kiri (masih none)
print("Data child kanan root:", root.right)     # menampilkan child kanan (masih none)

"""
# ==============================================
# Pembahasan:
# ==============================================

# Pada kode ini, kita membuat struktur dasar dari tree menggunakan class Node, 
# di mana setiap node memiliki tiga bagian utama yaitu data sebagai nilai yang disimpan, 
# serta left dan right sebagai penunjuk ke child kiri dan kanan. 
# Saat sebuah node pertama kali dibuat, nilai left dan right diatur ke None yang berarti node tersebut belum memiliki anak. 
# Selanjutnya dibuat sebuah root dengan nilai "A", yang berperan sebagai node utama atau paling atas dalam tree. 
# Ketika program dijalankan, root.data akan menampilkan "A", sedangkan root.left dan root.right masih bernilai None karena belum ada child yang ditambahkan. 
# Hal ini menunjukkan bahwa struktur tree sudah terbentuk namun masih sederhana tanpa cabang, 
# sehingga kode ini merupakan langkah awal sebelum mengembangkan tree menjadi lebih kompleks dengan menambahkan node-node lain sebagai child kiri dan kanan.
""" 
