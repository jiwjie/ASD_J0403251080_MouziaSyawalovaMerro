# Latihan 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:  # jika list kosong
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    # Fungsi pencarian
    def search(self, key):
        if not self.head:
            return False

        temp = self.head

        while True:
            if temp.data == key:
                return True
            temp = temp.next
            if temp == self.head:
                break

        return False


#==========================
#Program Utama
#==========================

print("==== Implementasi pencarian pada Circular Singly Linked List ====")

cll = CircularSinglyLinkedList()

#=============================
#Input data list
#=============================

while True:
    data_input = input("\nMasukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

    if data_input.strip() == "":
        print("Input tidak boleh kosong. Silakan ulangi.")
        continue

    data_list = data_input.split(",")
    valid = True

    # Validasi semua input 
    for item in data_list:
        if item.strip() == "":
            valid = False
            break
        try:
            int(item.strip())
        except ValueError:
            valid = False
            break

    if not valid:
        print("Input tidak sesuai perintah. Silakan ulangi.")
        continue

    # Masukkan ke list jika valid
    for item in data_list:
        cll.insert_at_end(int(item.strip()))

    break  # keluar dari while jika sukses


#===========================
#Input data yang dicari
#===========================

while True:
    cari_input = input("\nMasukkan elemen yang ingin dicari: ")

    try:
        cari = int(cari_input.strip())
        break
    except ValueError:
        print("Input harus berupa satu angka saja.")


#==========================
#Pencarian node
#==========================

if not cll.head:
    print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
else:
    if cll.search(cari):
        print(f"Elemen {cari} ditemukan dalam Circular Linked List.")
    else:
        print(f"Elemen {cari} tidak ditemukan dalam Circular Linked List.")
