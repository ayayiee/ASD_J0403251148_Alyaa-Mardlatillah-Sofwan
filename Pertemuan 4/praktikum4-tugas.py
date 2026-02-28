# ====================================
# Nama  : Alyaa Mardlatillah Sofwan
# NIM   : J0403251148
# Kelas : TPL B-1
#=====================================

# ==========================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ==========================================================

# Class Node untuk menyimpan data pelanggan
class Node:
    def __init__(self, no, nama, servis):
        self.no = no            # Nomor antrian
        self.nama = nama        # Nama pelanggan
        self.servis = servis    # Jenis servis
        self.next = None        # Pointer ke node berikutnya

# Class Queue berbasis Linked List
class Queuebengkel:
    def __init__(self):
        self.front = None        # Pointer ke pelanggan terdepan
        self.rear  = None        # Pointer ke pelanggan terakhir

        # ===========================
        # Enqueue : Tambah Pelanggan
        # ===========================

    def enqueue(self, no, nama, servis):
            new_node = Node(no, nama, servis)   # Membuat node baru

            if self.rear is None:               # Jika antrian kosong
                self.front = self.rear = new_node   
            else:
                self.rear.next = new_node       # Hubungkan node terakhir ke node baru
                self.rear = new_node            # Pindahkan rear ke node baru

            print("Pelanggan berhasil ditambahkan ke antrian.")

        # ==============================
        # Dequeue: Layani pelanggan
        # ==============================
    def dequeue(self):
            if self.front is None:  # Jika antrian kosong
                print("Antrian kosong. Tidak ada pelanggan untuk dilayani.")
                return
        
            dilayani = self.front  # Simpan pelanggan terdepan
            self.front = self.front.next  # Pindahkan front ke node berikutnya
            
            if self.front is None:  # Jika setelah dequeue antrian kosong
                self.rear = None
            
            print(f"Pelanggan {dilayani.nama} dengan No {dilayani.no} sedang dilayani.")

        # ==============================
        # Tampilkan seluruh antrian
        # ==============================
    def tampilkan(self):
            if self.front is None:
                print("Antrian kosong.")
                return
            
            print("\n ----- Daftar Antrian -----")
            current = self.front # Mulai traversal dari depan

            while current is not None: # Traversal sampai akhir
                print(f"No: {current.no} | Nama: {current.nama} | Servis: {current.servis}")
                current = current.next # Pindah ke node berikutnya

# ==============================
# Program Utama
# ==============================
def main ():
    q = Queuebengkel()

    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama      : ")
            servis = input("Servis    : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            print("Program selesai. Terima Kasih")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()