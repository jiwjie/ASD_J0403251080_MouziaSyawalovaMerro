#================================================= 
# Nama : Mouzia Syawalova Merro 
# NIM : J0403251080
# Kelas : TPL B2
#=================================================

#=================================================
# Latihan 6 : Rotasi Kanan pada BST tidak seimbang
#=================================================

#class Node
class Node:
    def __init__(self, data):
        self.data = data        # Menyimpan nilai data
        self.left = None        # child kiri
        self.right = None       # child kanan
        
# Fungsi preorder untuk melihat isi tree
'''membaca tree berurut dari root kebawah. dimulai dengan cetak node sekarang, menelusuri di bagian kiri sampai habis, lanjut ke kanan'''

def preorder (root):
    if root is not None:
        print(root.data, end=" ")       #cetak data root
        preorder(root.left)             #rekursif ke child kiri
        preorder(root.right)            #rekursif ke child kanan
        
# Fungsi untuk menampilkan struktur tree
'''menampilkan bentuk tree di layar biar seperti hierarki. spasi digunakan tiap turun level untuk indentasi'''

def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}")     #memberi indentasi sesuai level 
        tampil_struktur(root.left, level + 1, "L")      #cetak child kiri
        tampil_struktur(root.right, level + 1, "R")     #cetak child kanan
        
# Fungsi rotasi kanan 
'''digunakan saat pohon miring ke kiri, kebalikan dari rotasi kiri. 
child kiri ditarik jadi root, dan root lama akan menjadi child kanan.'''

def rotate_right(y): 
    # y adalah root lama 
    x = y.left       # x adalah child kiri y
    T2 = x.right       # ambil subtree kanan milik x untuk dipindahkan

    # Proses rotasi 
    x.right = y        # y turun menjadi child kanan dari x
    y.left = T2      # subtree T2 yang semula child kanan x, jadi child kiri y
    
    # x menjadi root baru 
    return x

#===============================================================
# Program Utama
#===============================================================

# Membuat tree yang tidak seimbang
# 30 -> 20 -> 10

root = Node(30)     # root utama
root.left = Node(20)        #child kiri 30
root.left.left = Node(10)       #child kiri dari 20

print ("Preorder sebelum rotasi kanan: ")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan: ")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)

print("\nPreorder sesudah rotasi kanan: ")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan: ")
tampil_struktur(root)

# alur 
'''pohon akan membentuk garis lurus ke bawah pada awal kita memasukkan data.
kemudian rotate_right akan menarik node tengah untuk jadi root. 
node 30 akan jadi child kanan. pohon yang tadinya tidak seimbang, menjadi seimbang 
dengan 20 sebagai root, 10 di kiri, 30 di kanan.'''