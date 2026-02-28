# ===================================================================
# Nama: Alyaa Mardlatillah Sofwan
# NIM: J0403251148
# Kelas: TPL B-1
# ===================================================================

# ===================================================================
# Studi Kasus: Sistem Antrian Layanan Akademik
# Implementasi Queue =>
# Enqueue : Memindahkan Pointer Rear (nambah data baru dari belakang)
# Dequeue : Memindahkan Pointer Front (menghapus data dari depan)
# Front -> A -> B -> C -> Rear (ini Queue)
# Stack ==> Front -> C - B - A
# ====================================================================

# 1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim    = nim  # Menyimpan nim mahasiswa
        self.nama   = nama # Menyimpan nama  mahasiswa
        self.next   = None # Pointer ke node berikutnya

# 2) Mendefinisikan Queue terdiri dari font dan rear
class queueAkademik:
    def __init__(self):
        self.front  = None # depan
        self.rear   = None # belakang

    def is_empty(self):
        # Ketika queue kosong maka front = rear = none
        return self.front is None
    
    # Menambahkan data beru ke bagian belakang (rear) =>  menambahkan antrian mahasiswan yang akan mengajukan layanan akademik
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)
        # Jika data baru dari Queue yang kosong, maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru 
            self.rear = nodeBaru
            return
        #  Jika Queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        else:
            self.rear.next = nodeBaru
            self.rear = nodeBaru

    # Menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty():
            print("Antrian Kosong. Tidak ada mahasiswa yang dilayani")
            return None
        
        # Lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        # Geser pointer front ke next front
        self.front = self.front.next

        # Jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None
        return node_dilayani
    
    # Menampilkan
    def tampilkan(self):
            
            print("\nDaftar Antrian Mahasiswa (Front -> Rear): ")
            current = self.front
            no = 1
            while current is not None:
                print(f"{no}. {current.nim} - {current.nama}")
                current = current.next
                no += 1

# Program Utama
def main():
    
    # Instansi Queue
    q = queueAkademik()

    while True:
        print("======== Tambah Mahasiswa ========")
        print("1. Tambah Mahasiswa ")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            nim = input("Masukkan  NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()

            q.enqueue(nim, nama)
            print("Mahasiswa Berhasil Ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program Selesai. Terimakasih")
        else: 
            print("Pilihan tidak valid. Silahkan coba lagi 1-4")

# Penanda eksekusi file utama
if __name__ == "__main__":
    main()
        






















































































































