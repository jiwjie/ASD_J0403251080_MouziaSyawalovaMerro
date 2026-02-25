#========================================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
#========================================================================

#========================================================================
# Studi Kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue =>
# Enqueue : memindahkan pointer rear (nambah data baru dari belakang)
# Dequeue : memindahkan pointer head (menghapus data dari depan)
# Front -> A -> B -> C -> Rear
#========================================================================

# 1. Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self,nim,nama):
        self.nim = nim    #menyimpan NIM mahasiswa
        self.nama = nama   #menyimpan Nama mahasiswa
        self.next = None   #pointer ke node berikutnya 
    
# 2. Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        # Ketika queue kosong, maka front = rear = none
        return self.front is None
    
    # menambahkan data baru ke bagian belakang (rear) => menambahkan antrian mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)
        # jika data baru masuk dari enqueue yang kosong maka data baru = front = rear
        if self.is_empty():     
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan rear
        
        self.rear.next = nodeBaru
        self.rear = nodeBaru
    
    # menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):
        
        if self.is_empty():
            print("Antrian Kosong. Tidak ada Mahasiswa yang dilayani. ")
            return None
        
        # lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        nodeDilayani = self.front
        
        # geser pointer front ke next front
        self.front = self.front.next
        
        # jika front menjadi none (data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None
        return nodeDilayani
    
    # menampilkan
    def tampilkan(self):
        
        print("\nDaftar Antrian Mahasiswa (Front -> Rear) : ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next 
            no += 1     

# Program Utama 
def main():
    
    #instatiasi queue
    q = queueAkademik()
    
    while True:
        print("==== Sistem Antrian Akademik ====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("Pilih Menu (1-4) : ").strip()
        
        if pilihan == "1":
            nim = input("\nMasukkan NIM Mahasiswa : ").strip()
            nama = input("Masukkan Nama Mahasiswa : ").strip()
            
            q.enqueue(nim, nama)
            print("\nMahasiswa berhasil ditambahkan ke antrian")
            
        elif pilihan == "2":
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")
            
        elif pilihan == "3":
            q.tampilkan()
            
        elif pilihan == "4":
            print("\nProgram selesai. Terimakasih")
        
        else: 
            print("\nPilihan tidak valid. Silahkan coba lagi 1-4")
            
# penanda eksekusi file utama
if __name__ == "__main__":
    main()
            