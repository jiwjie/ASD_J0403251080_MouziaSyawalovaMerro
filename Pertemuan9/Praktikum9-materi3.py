#===========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : B - B2
#===========================================================

#===========================================================
# Latihan 3 : Membuat Traversal Preorder
#===========================================================

#class Node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # child kiri
        self.right = None   # child kanan
        
# fungsi preorder degan aturan:  root -> left -> right
def preorder (node):
    if node is not None:        # cek apakah node kosong atau tidak
        print(node.data, end=" ")       # mencetak data dari node yang sedang dikunjungi (root)
        preorder(node.left)             # menelusuri cabang kiri
        preorder(node.right)            # menelusuri cabang kanan
    
# membuat tree
# membuat sebuah node root
root = Node("A")
    
    # membuat child level 1
root.left = Node("B")
root.right= Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")


# menjalankan traversal preorder
print("Hasil Traversal Preorder : ")
preorder(root)



# penjelasan
''' Disini kita menerapkan preorder tranversal dengan prinsip mengunjungi induk dahulu baru anak-anaknya.
Alur ini diatur oleh fungsi preorder() yang menggunakan logika rekursif,
di mana program akan terus memanggil dirinya sendiri untuk masuk ke setiap cabang yang ada.
Saat program sampai di sebuah node, data akan dicetak.
Lalu, diprioritaskan untuk menelusuri seluruh cabang sebelah kiri sampai tidak ada yang bisa dikunjungi.
Jika sisi kiri sudah selesai, program akan naik dan mulai ke bagian kanan.
Saat diterapkan, program memulai dari A, ke kiri yaitu B, lalu ke ujung kiri "D".
Karena setelah D tidak ada cabang lagi, program bergeser ke kanan untuk mencetak E.
Baru mencetak ke E, kemudian ke sisi kanan yakni C,F, dan G. 
Sehingga terbentuklah urutan A B D E C F G
'''