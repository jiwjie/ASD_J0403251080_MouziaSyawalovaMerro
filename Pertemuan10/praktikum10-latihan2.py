#================================================= 
# Nama : Mouzia Syawalova Merro 
# NIM : J0403251080
# Kelas : TPL B2
#=================================================

#=================================================
# Latihan 4 : Membuat BST yang tidak seimbang
#=================================================

# class node untuk menyimpan data BST

class Node:
    def __init__(self, data):
        self.data = data        # nilai pada node
        self.left = None        # child kiri
        self.right = None       # child kanan
    
# Alur fungsi insert pada BST 
''' fungsi untuk memasukkan data ke tree. kalau data lebih kecil maka dia akan mengecek ke bagian kiri.
kalau data lebih besar, maka akan di cek ke kanan sampai ada tempat kosong.'''

def insert(root,data):
    # jika root kosong, buat node baru
    if root is None:
        return Node(data)

    # jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    
    # jika data lebih besar, masuk ke subtree kanan    
    elif data > root.data:
        root.right = insert(root.right, data)
            
    return root
    
# Fungsi preorder untuk melihat bentuk tree
'''fungsi untuk membaca tree dengan urutan :
> mencetak node sekarang, menelusuri cabang kiri, lanjut ke cabang kanan'''

def preorder (root):
    if root is not None:
        print(root.data, end=" ")       # cetak data root
        preorder(root.left)             # rekursif cabang kiri
        preorder(root.right)            # rekursif cabang kanan
        
# Fungsi sederhana untuk menampilkan struktur tree
'''menampilkan bentuk tree di layar biar seperti hierarki. spasi digunakan tiap turun level untuk indentasi'''

def tampilkan_struktur(root, level = 0, posisi = "Root") :
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")      # memberi indentasi berdasarkan level
        tampilkan_struktur(root.left, level+1, "L")         #cetak child kiri 
        tampilkan_struktur(root.right, level+1, "R")        # cetak child kanan
        
        
#==============================================================
# Program utama
#==============================================================

root = None

# Data dimasukkan berurutan naik
data_list = [10,20,30]

for data in data_list:
    root = insert(root, data)

print("Preorder BST : ")
preorder(root)

print("\n\n Struktur BST :")
tampilkan_struktur(root)


# penjelasan
'''
1. Tree condong ke kanan
> karena data dimasukkan berurutan naik dari 10,20,dan 30, fungsi insert akan 
memahami bahwa data baru lebih besar dari root. Jadi, tree tidak punya anak kiri. 
Bentuknya akan seperti garis lurus ke bawah, bukan seperti pohon

2. Semakin panjang tree, pencarian semakin lambat
> Dalam BST yang seimbang, pencarian data memiliki kompleksitas waktu O(log n).
Kalau pohon tidak seimbang, maka pencarian berupa linear search (O(n)).
Jika data banyak dan terurut, pencarian bisa memakan waktu sangat lama karena menelusuri 
satu persatu

3. BST tidak selalu seimbang
> keseimbangan BST bergantung pada urutan data yang dimasukkan.
disini memakai aturan: kiri lebih kecil, kanan lebih besar.'''

# alur
'''fungsi insert otomatis membandingkan nilai baru dengan yang sudah ada. jika nilai baru lebih besar, 
maka diletak di kanan. karena angka yang kita masukkan selalu lebih besar (menaik), maka tiap angka baru akan mengisi di kanan.
sehingga pohon memanjang ke bawah.'''