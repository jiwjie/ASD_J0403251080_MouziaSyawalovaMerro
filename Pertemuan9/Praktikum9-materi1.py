#===========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : B - B2
#===========================================================

#===========================================================
# Latihan 1 : Membuat Node
#===========================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai utama dari node
        self.left = None    # menyimpan child kiri
        self.right = None   # menyimpan child kanan
        
# membuat root
root = Node("A")

# menampilkan isi node 
print("Data pada root : ",root.data)
print("Data child kiri : ",root.left)
print("Data child kanan : ",root.right)
    
    # pembahasan 
    