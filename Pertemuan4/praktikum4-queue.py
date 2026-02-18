#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Implementasi Dasar : Node pada List
#================================================================

#membuat class node 
class Node:
    def __init__(self, data):
        self.data = data        #menyimpan nilai/data
        self.next = None        #pointer ke node berikutnya (awal=none)
        
# Queue dengan 2 pointer : front and rear / head and tail
class QueueLL:
    def __init__(self):
        self.front = None   #Node paling depan
        self.rear = None    #node paling belakang
        
        
    def is_empty(self):
        return self.front is None
        
    def enqueue(self,data):
        #menambah data dibelakang (rear)
        nodeBaru = Node(data)
        
        
        #jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong:
        #rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #rear pindah ke node baru
        self.rear  = nodeBaru
    
    def dequeue (self):
        #menghapus data dari depan
        
        
        # 1. lihat data yang paling depan
        data_terhapus = self.front.data
        
        # 2. geser front ke node berikutnya
        self.front = self.front.next
        
        # 3. jika setelah geser front menjadi none, maka queue kosong
        # rear juga harus jadi none
        if self.front is None:
            self.rear = None
            
        return data_terhapus
    
    def tampilkan(self):
        #menampilkan isi queue dari front ke rear
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear di node terakhir")
        
    #instantiasi objek class QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()