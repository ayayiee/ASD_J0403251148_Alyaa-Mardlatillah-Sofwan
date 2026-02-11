# =========================================================================
# Pertemuan : 3
# Latihan 1: Implementasi fungsi untuk menghapus node dengan nilai tertentu
# =========================================================================

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #fungsi untuk menambah node di akhir
    def append(self, data):
        new_node = Node(data)

        if not self.head: # jika linked list masih kosong
            self.head = new_node
            return
            
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    #menghapus node sesuai nilai
    def delete_node(self, key):
            temp = self.head # mulai dari head

            #kalau node yang mau dihapus adalah head
            if temp and temp.data == key: # cek apakah head berisi key
                self.head = temp.next # head pindah ke node berikutnya
                temp = None
                print("Data berhasil dihapus.")
                return
            
            prev = None # penunjuk node sebelumnya
            while temp and temp.data != key: # cari node yang sesuai key
                prev = temp
                temp = temp.next

            #kalau data tidak ditemukan
            if temp is None:
                print(f"Data tidak ditemukan.")
                return
            
            prev.next = temp.next # lewati node yang ingin dihapus
            temp = None
            print("Data berhasil dihapus.")

    #menampilkan isi linked list
    def display(self):
        temp = self.head
        if temp is None:
            print("Linked list kosong.")
            return
                
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("null")

# Program utama
ll = LinkedList()

#input jumlah data
print(" ==== Implementasi fungsi menghapus node ==== ")
n = int(input("Masukkan jumlah data: "))

for i in range(n):
    data = int(input(f"Masukkan data ke-{i+1}: ")) # input data satu per satu
    ll.append(data) # masukkan ke linked list

print("\nIsi Linked List: ")
ll.display() # tampilkan isi sebelum dihapus

#input nilai yang ingin dihapus
hapus = int(input("\nMasukkan nilai yang ingin dihapus: "))
ll.delete_node(hapus) # panggil fungsi hapus

print("\nLinked list setelah dihapus")
ll.display() # tampilkan hasil setelah dihapus
