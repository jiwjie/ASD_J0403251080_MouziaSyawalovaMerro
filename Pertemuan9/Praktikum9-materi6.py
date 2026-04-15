#===========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : B - B2
#===========================================================

#===========================================================
# Latihan 6 : Struktur Organisasi Perusahaan
#===========================================================

#class Node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # menyimpan child kiri
        self.right = None   # menyimpan child kanan
        

def preorder (node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
       
# membuat struktur organisasi 
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")
root.right.right = Node("Staff 3")

# menjalankan traversal preorder
print("Struktur Organisasi (preorder) :")
preorder(root)

#penjelasan
'''
kita menerapkan konsep Binary Tree ke dalam skenario nyata berupa struktur organisasi perusahaan dengan menggunakan metode Preorder Traversal.
penelusuran dimulai tepat dari posisi paling atas yaitu Direktur sebagai root.
Melalui fungsi preorder(), program akan mencatat nama pimpinan terlebih dahulu, kemudian langsung turun menelusuri seluruh
jajaran di bawah Manajer A (termasuk Staff 1 dan Staff 2) hingga tuntas, barulah setelah itu ia berpindah untuk memeriksa jajaran di bawah Manajer B (yaitu Staff 3).
Ini memetakan hubungan atasan dan bawahan secara hierarkis, sehingga hasil akhirnya memberikan gambaran urutan dari "bos besar" turun ke cabang kiri hingga habis, baru kemudian cabang kanan.
'''
