#================================================= 
# Nama : Mouzia Syawalova Merro 
# NIM : J0403251080
# Kelas : TPL B2
#=================================================

#=================================================
# Latihan 5 : Rotasi Kiri pada BST tidak seimbang
#=================================================

#class Node
class Node:
    def __init__(self, data):
        self.data = data        # menyimpan nilai pada node
        self.left = None        # child kiri
        self.right = None       # child kanan 
        
# Fungsi preorder untuk melihat isi tree
'''membaca tree berurut dari root kebawah. dimulai dengan cetak node sekarang, menelusuri di bagian kiri sampai habis, lanjut ke kanan'''

def preorder (root):
    if root is not None:
        print(root.data, end=" ")       # mencetak data pada node sekarang
        preorder(root.left)             # rekursif ke child kiri
        preorder(root.right)            # rekursif ke child kanan
        
# Fungsi untuk menampilkan struktur tree
'''menampilkan bentuk tree di layar biar seperti hierarki. spasi digunakan tiap turun level untuk indentasi'''

def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}")     # memberi indentasi berdasarkan level
        tampil_struktur(root.left, level + 1, "L")          # cetak child kiri
        tampil_struktur(root.right, level + 1, "R")         # cetak child kanan
        
# Fungsi rotasi kiri 
'''cara untuk menyeimbangkan pohon yang miring ke kanan.
child di kanan ditarik jadi root. root lama akan turun menjadi child kiri'''

def rotate_left(x): 
    # x adalah root lama 
    y = x.right       # y adalah child kanan x 
    T2 = y.left       # subtree kiri milik y disimpan sementara

    # Proses rotasi 
    y.left = x        # x menjadi child kiri dari y 
    x.right = T2      # child kanan x diganti dengan T2
    
    # y menjadi root baru 
    return y

#===============================================================
# Program Utama
#===============================================================

# Membuat tree yang tidak seimbang
# 10 -> 20 -> 30

root = Node(10)     # root awal 
root.right = Node(20)       # child kanan dari 10
root.right.right = Node(30)     # child kanan dari 20

print ("Preorder sebelum rotasi kiri: ")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri: ")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri: ")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri: ")
tampil_struktur(root)

#alur
'''node 20 sebagai node tengah ditarik ke ats untuk menjadi root, sementara node lama yakni 10 
akan menjadi child kiri. rotate_left akan memastikan jika ada cabang perantara dan posisinya mengikuti BST dengan
memindahkan ke sisi kanan node yg turun. hasilnya, pohon menjadi seimbang dengan 20 sebagai root, 10 di kiri, 30 di kanan.'''
