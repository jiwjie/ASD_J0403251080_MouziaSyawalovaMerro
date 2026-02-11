#Latihan 1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    #Fungsi untuk menambah node di akhir 
    def append(self, data):
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
    #Menghapus node sesuai nilai
    def delete_node (self,key):
        temp = self.head
        
        #jika node yang ingin dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            print("Data berhasil dihapus!")
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        
        #jika data tidak ditemukan
        if temp is None:
            print (f'Data tidak ditemukan!')
            return
        
        prev.next = temp.next
        temp = None
        print("Data berhasil dihapus!")
        
        #menampilkan isi linked list
    def display(self):
        temp = self.head
        if temp is None:
            print("Linked list kosong.")
            return
            
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
            
#=========================================
# Program Utama
#=========================================

ll = LinkedList()

#Input jumlah data
print("==== Implementasi fungsi menghapus node ==== ")
n = int(input("\nMasukkan jumlah data : "))

for i in range(n):
    while True:
        try:
            data = int(input(f"Masukkan data ke-{i+1} : "))
            ll.append(data)
            break
        
        except ValueError: 
            print("\nInputan tidak sesuai! Masukkan sebuah angka.")
    
print("\nIsi Linked List : ")
ll.display()

#Input nilai yang ingin dihapus 
hapus = int(input("\nMasukkan nilai yang ingin dihapus : "))
ll.delete_node(hapus)

print("\nLinked list :")
ll.display()
print("=== Selesai! ===")