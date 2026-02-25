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
        self.next = None
        
class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue (self, no, nama, servis):
        # Tambahkan data ke antrian
        dataBaru = Node(no, nama, servis)
        
        # jika data kosong, maka data baru = front = rear
        if self.is_empty():
            self.front = dataBaru
            self.rear = dataBaru
            return
    
        # jika data tidak kosong, maka data baru diletakkan setelah rear
        self.rear.next = dataBaru
        self.rear = dataBaru
        
    # Melayani pelanggan terdepan  
    def dequeue(self):
        if self.is_empty():
            print("Antrian Kosong. Tidak ada pelanggan yang bisa dilayani.")
            return None
        
        node_dilayani = self.front
        
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
            return node_dilayani
        
    # Tampilkan seluruh antrian
    def tampilkan(self):
        
        print("\n=== Daftar Antrian Pelanggan Bengkel ===")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nama} | {current.servis}")
            current = current.next
            no += 1
            
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
            print("\nPelanggan berhasil ditambahkan.")
        
        elif pilih == "2":
            dilayani = q.dequeue()
            print(f"Pelanggan no-{no} atas nama {nama} telah selesai dilayani.")
                
        elif pilih == "3":
            q.tampilkan()
            
        elif pilih == "4":
            break
            
        else:
            print("Pilihan tidak valid. Coba sekali lagi.")
            return
            
if __name__ == "__main__":
    main()