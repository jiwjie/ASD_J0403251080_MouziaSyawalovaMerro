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
    
    # pembahasan dari kode
''' Di kode ini merupakan langkah awal dalam membangun struktur pohon biner dengan cara 
membentuk sebuah bernama class Node dahulu. Di sini, terdapat fungsi khusus init yang bertugas menyiapkan wadah 
setiap kali sebuah titik baru dibuat, yaitu self.data sebagai tempat menyimpan nilai, serta self.left dan self.right yang berfungsi sebagai 
penghubung ke "child" nanti. Lalu, dibentuk sebuah root yang memilki nilai "A". Disini kita baru membentuk root tanpa ada "child" dahulu, sehingga kedua penghubungnya kosong/bernilai None. 
Jadi, inti dari proses ini adalah menyiapkan fondasi paling atas agar nantinya kita bisa menyambungkan data-data lain ke cabang kiri maupun kanan hingga membentuk satu kesatuan pohon yang utuh.
