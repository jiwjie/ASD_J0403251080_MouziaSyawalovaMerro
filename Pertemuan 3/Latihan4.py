class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  
        
    # Fungsi tambah data 
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    def display(self):
        current = self.head
        
        # Jika list kosong
        if current is None:
            print("List kosong.")
            return

        # Perulangan biasa 
        while current is not None:
            # Cetak angka
            print(current.data, end="")
            
            # Cetak panah
            print(" -> ", end="")
            
            # Pindah ke node berikutnya
            current = current.next
            
        print("null") # Penutup di paling belakang

# Logika menggabungkan list
def gabung_linked_list(list1, list2):
    list_baru = LinkedList()

    # Loop untuk memindahkan isi list pertama
    current = list1.head
    while current is not None:
        list_baru.insert_at_end(current.data)
        current = current.next

    # Loop untuk memindahkan isi list kedua
    current = list2.head
    while current is not None:
        list_baru.insert_at_end(current.data)
        current = current.next

    return list_baru

# Fungsi meminta input 
print("==== Menggabungkan dua single linked list menjadi satu linked list baru ====")
def buat_list_dari_input(urutan):
    ll = LinkedList()
    print(f"\n=== Input Linked List {urutan} ===")
    print("Masukkan angka (pisahkan dengan spasi). Tekan Enter jika selesai.")
    
    data_input = input(f"Isi List {urutan}: ")
    
    # Cek jika kosong
    if data_input == "":
        return ll

    # Memecah input menjadi angka
    angka_list = data_input.replace(',', ' ').split()
    
    for item in angka_list:
        ll.insert_at_end(int(item))
            
    return ll

#==========================================
#Main Program
#==========================================

#Input data
list1 = buat_list_dari_input("1")
list2 = buat_list_dari_input("2")

#Tampilkan data awal
print("\n==== Hasil ====")
print("Linked List 1:", end=" ")
list1.display()

print("Linked List 2:", end=" ")
list2.display()

# Menggabungkan dan menampilkan list
print("Linked List setelah digabungkan:", end=" ")
hasil_gabungan = gabung_linked_list(list1, list2)
hasil_gabungan.display()