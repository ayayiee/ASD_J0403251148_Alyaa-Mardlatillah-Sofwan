#==============================================
# Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 1A : Membaca seluruh isi file
#==============================================

#membuka file dengan mode read ("r")

#mebuka file dalam satu string
with open("J0403251148_Alyaa Mardlatillah Sofwan_B1_Pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read() #membaca keseluruhan isi file dalam satu string
print(isi_file)

print("=== Hasil Read ===")
print("Tipe Data: ", type(isi_file))
print("Jumlah Karakter: ", len(isi_file))
print("Jumlah Baris: ", isi_file.count("\n")+1)

#membuka file per baris
print("=== Membaca File per Baris ===")
jumlah_baris = 0
with open("J0403251148_Alyaa Mardlatillah Sofwan_B1_Pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #menghilangkan baris baru
        print("Baris ke-", jumlah_baris)
        print("Isinya: ", baris)

#mensplit/memisahkan satu data dengan yang lain
with open("J0403251148_Alyaa Mardlatillah Sofwan_B1_Pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM: ", nim, "| Nama: ", nama, "| Nilai: ", nilai)


#======================================================
# Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca file dan Menyimpan ke List
#======================================================

data_list = [] #list untuk menampung data mahasiswa

with open("J0403251148_Alyaa Mardlatillah Sofwan_B1_Pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan sebagai list "[nim, nama, nilai]"
        data_list.append([nim, nama, int(nilai)])

print("==== Data Mahasiswa dalam LIST ====")
print(data_list)

print("==== Jumlah Record dalam LIST ====")
print("Jumlah Record", len(data_list)) 

print("==== Menampilkan Data Record Tertentu ====")
print("Contoh Record Pertama: ", data_list[0]) #array dimulai dari 0


#=========================================================
# Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca file dan Menyimpan ke Dictionary
#==========================================================

data_dict = {} #buat variabel untuk dictionary 
with open("J0403251148_Alyaa Mardlatillah Sofwan_B1_Pertemuan 1/data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan baris baru
        nim, nama, nilai = baris.split(",")

        #simpan data mahasiswa ke dictioanary dengan key NIM
        data_dict[nim] = {          #key
            "nama" : nama,          #values
            "nilai" : int(nilai)    #values
        }
print("==== Data Mahasiswa dalam Dictionary ====")
print(data_dict)