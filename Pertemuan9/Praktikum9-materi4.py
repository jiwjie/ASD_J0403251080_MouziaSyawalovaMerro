#===========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : B - B2
#===========================================================

#===========================================================
# Latihan 4 : Membuat Traversal Inorder
#===========================================================

#class Node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # menyimpan child kiri
        self.right = None   # menyimpan child kanan
        
# membuat fungsi inorder : left > root> right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)
        
        
# membuat tree
# membuat sebuah node root
root = Node("A")
    
# membuat child level 1
root.left = Node("B")
root.right= Node("C")
    
# membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

print("Hasil Traversal Inorder : ")
inorder(root)

# penjelasan 
'''kita mempraktikkan metode Inorder Traversal yang memiliki ciri khas urutan "Kiri-Tengah-Kanan".
program akan menyelam ke bagian kiri paling dasar dan mencetaknya (D).
baru kemudian naik satu tingkat untuk mencetak induknya (B),
dan mengecek apakah ada cabang di sebelah kanan (E).
Logika ini terus berlanjut hingga seluruh sisi kiri selesai, barulah titik pusat utama (root A) dicetak,
dan lanjut program berpindah untuk memproses sisi kanan dengan pola yang sama.
Alur ini akan menghasilkan urutan D B E A C
'''