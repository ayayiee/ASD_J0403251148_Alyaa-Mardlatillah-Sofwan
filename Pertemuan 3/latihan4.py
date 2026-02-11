# ===============================================================================================
# Pertemuan : 3
# Latihan 4: Buat Metode untuk Menggabungkan Dua Single Linked List Menjadi Satu Linked List Baru
# ===============================================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #fungsi tambah data di akhir 
    def insert_at_end(self, data):
        new_mode = Node(data)

        if not self.head: # jika linked list masih kosong, node baru jadi head sekaligus tail
            self.head = new_mode
            self.tail = new_mode
        else:
            self.tail.next = new_mode # sambungkan tail lama ke node baru
            self.tail = new_mode # pindahkan tail ke node baru

    #fungsi untuk menampilkan isi linked list
    def display(self):
        current = self.head # mulai dari head 

        #jika list kosong
        if current is None:
            print("Kosong")
            return
        
        #perulangan biasa
        while current is not None:
            print(current.data, end="") # tampilkan data
            print("->",end="") # tampilkan panah
            current = current.next # pindah ke node berikutnya
        
        print("null") #penutup di paling belakang

#fungsi untuk gabungkan 2 linked list
def gabung_linked_list(list1, list2):
    list_baru = LinkedList()

    #pindahkan semua isi list 1 ke list baru
    current = list1.head
    while current is not None:
        list_baru.insert_at_end(current.data) # masukkan data ke list baru
        current = current.next

    #pindahkan semua isi list 2 ke list_baru
    current = list2.head
    while current is not None:
        list_baru.insert_at_end(current.data) # masukkan data ke list baru
        current = current.next

    return list_baru # kembalikan hasil gabungan


#fungsi untuk input data
def buat_list_dari_input(urutan): 
    ll = LinkedList() #buat linked list kosong

    print(f"\n --- Input Linked List {urutan} ---")
    print("Masukkan angka (pisahkan dengan spasi). Tekan enter jika selesai.")

    data_input = input(f"Isi List {urutan}: ")

    #jika user tidak memasukkan apa-apa
    if data_input == "":
        return ll #kembalikan linked list kosong
    
    #mengubah koma jadi spasi lalu dipecah
    angka_list = data_input.replace(",", " ").split()

    #masukkan setiap angka ke linked list
    for item in angka_list:
        ll.insert_at_end(int(item))
    return ll

# === Main Program ===

# input data dari user 
list1 = buat_list_dari_input("1") #buat linked list 1
list2 = buat_list_dari_input("2") #buat linked list 2

#tampilkan data awal
print("\n ------- Hasil ------")
print("Linked list 1:", end=" ")
list1.display() #tampilkan isi list 1

print("Linked list 2:", end=" ")
list2.display() #tampilkan isi list 2

print("Linked List setelah digabungkan: ", end="")
hasil_gabung = gabung_linked_list(list1, list2)
hasil_gabung.display() #tampilkan hasil