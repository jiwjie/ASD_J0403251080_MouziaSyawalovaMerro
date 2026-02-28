#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Tugas Hands-On : Sistem Antrian Bengkel Motor
#================================================================

class Node: 
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None        # pointer untuk menunjuk ke pelanggan berikutnya
        
class QueueBengkel:
    def __init__(self):
        # menginisialisasi pointer front dan rear
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue (self, no, nama, servis):
        # Tambahkan data ke antrian
        nodeBaru = Node(no, nama, servis)
        
        # jika antrian kosong, maka front dan rear akan menunjuk ke node baru
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            print(f"Berhasil menambahkan {nama} ke antrian.")
            return
    
        # jika antrian tidak kosong, maka data baru diletakkan setelah rear (dibelakang antrian)
        self.rear.next = nodeBaru
        # memindahkan pointer rear ke node paling baru 
        self.rear = nodeBaru
        print(f"Berhasil menambahkan {nama} ke antrian.")
        
    # Melayani pelanggan terdepan  
    def dequeue(self):
        
        # jika antrian kosong, tidak ada pelanggan yang bisa dilayani
        if self.is_empty():
            print("Antrian Kosong. Tidak ada pelanggan yang bisa dilayani.")
            return None
        
        # menyimpan data pelanggan yang dilayani adalah pelanggan yang berada di depan 
        pelangganDilayani = self.front
        
        # menggeser pointer front ke node berikutnya / menghapus pelanggan paling depan dari antrian
        self.front = self.front.next
        
        # jika setelah digeser pelanggan pertama menjadi kosong, maka antrian habis
        if self.front is None:
            self.rear = None        # rear juga menjadi kosong
            return pelangganDilayani
        
        print(f"Selesai melayani pelanggan no{pelangganDilayani.no}. {pelangganDilayani.nama} | Jenis servis :{pelangganDilayani.servis} ")
    
    # Tampilkan seluruh antrian
    def tampilkan(self):
        
        print("\n=== Daftar Antrian Pelanggan Bengkel ===")
        print(f"{'No': <2} | {'Nama': <8} | {'Servis': >5}")
        # memulai transversal (penelusuran) dari node terdepan
        current = self.front
        no = 1
        
        # selama node tidak kosong, cetak antrian lalu geser ke antrian berikutnya
        while current is not None:
            print(f"{no : <3}| {current.nama : <8} | {current.servis : >5}")
            current = current.next
            no += 1
        print("=============================")
            
def main():
    q = QueueBengkel()
        
    while True:
        print("\n==== Sistem Antrian Bengkel ====")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
            
        pilih = input("Pilih menu : ")
            
        if pilih == "1":
            no = input("Masukkan no antrian : ")
            nama = input("Masukkan nama pelanggan : ")
            servis = input("Jenis servis : ")
            q.enqueue(no, nama, servis)
        
        elif pilih == "2":
            q.dequeue()
                   
        elif pilih == "3":
            q.tampilkan()
            
        elif pilih == "4":
            print("Terimakasih telah menggunakan sistem antrian bengkel.")
            print("=====================================================")
            break
            
        else:
            print("Pilihan tidak valid. Coba sekali lagi.")
            return
            
if __name__ == "__main__":
    main()