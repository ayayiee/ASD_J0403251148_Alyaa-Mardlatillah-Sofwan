# ====================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
#=====================================

# ====================================
# Implementasi Dasar: Node pada List
# ====================================

# Membuat class node 
class Node:
    def __init__(self, data): #konstruktor 
        self.data = data # menyimpan nilai/data
        self.next = None # menginisialisasi pointer ke note berikutnya (awal = none)

# 1) Membuat node satu per satu
nodeA = Node("A") #proses memanggil konstruktor dengan cara memanggil nama class nya
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None 
nodeA.next = nodeB # nodeA.next adalah node B (setelah A nya)
nodeB.next = nodeC 

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal -> menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data) # menampilkan data pada node saat ini
    current = current.next # pindah ke node berikutnya

# =====================================================
# Implementasi Dasar : Linked List + Insert Awal 
# =====================================================

class linkedlist:
    def __init__(self): # class implementasi Stack
        self.head = None # awalnya kosong

    def insert_awal(self, data): # push dalam stack
        # 1) Buat node baru
        nodeBaru = Node(data) # panggil class node

        # 2) node baru menunjuk ke head lama
        nodeBaru.next = self.head

        # 3) head pindah ke node baru
        self.head = nodeBaru 

    def hapus_awal(self): # pop dalam stack
        data_terhapus = self.head.data # peek dalam stack (peek -> melihat data paling depan/head tanpa menghapus dulu)
        # menggeser head ke node berikutnya (adalah proses menghapus)
        self.head = self.head.next
        print("Node yang dihapus adalah: ", data_terhapus)

    def tampilkan(self): # implementasi traversal
        current = self.head
        while current is not None:
            print (current.data)
            current = current.next

print("==== List Baru ====")
ll = linkedlist () # instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()


















































