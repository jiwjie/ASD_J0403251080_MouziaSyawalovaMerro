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
        self.next = None        #menginisialisasi pointer ketika  dijalankan #pointer ke node berikutnya (awal=none)
        
#  1) Membuat node satu per satu    
nodeA = Node ("A")      #proses memanggil konstruktor dg memanggil nama class
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node A -> B -> C -> None
nodeA.next = nodeB  #node B terletak di node A next
nodeB.next = nodeC

# 3) Menentukan node pertama / head
head = nodeA

# 4) Traversal : menelusuri dari head sampai none 
current = head
while current is not None:
    print(current.data)     #menampilkan data pada node saat ini
    current = current.next  #pindah ke node berikutnya
    
    
#================================================================
# Implememtasi Dasar : Linked List + Insert Awal 
#================================================================

class LinkedList :      #class implementasi stack
    def __init__(self):
        self.head = None    #awalnya kosong
        
    
    def insert_awal(self,data):    #push dalam stack
        # 1.    BUAT NODE BARU
        nodeBaru = Node(data)       #panggil class node
            
        # 2.    node baru menunjuk ke head lama 
        nodeBaru.next = self.head
        
        #3.     head pindah ke node baru
        self.head = nodeBaru
    def hapusAwal  (self):   # pop dalam stack
        data_terhapus = self.head.data   #peek dalam stack
        # menggeser head ke node berikutnya
        self.head = self.head.next
        print("Node yang dihapus adalah : ", data_terhapus)
        
        
    def tampilkan (self):       # implementasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
print("==== List Baru ====")
ll = LinkedList()       # instantiasi objek ke class Linked List
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z")
ll.tampilkan()
ll.hapusAwal ()
ll.tampilkan()