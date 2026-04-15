#===========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : B - B2
#===========================================================

#===========================================================
# Latihan 5 : Membuat Traversal Postorder
#===========================================================

#class Node adalah unit dasar pada tree

class Node:
    def __init__(self, data):
        self.data = data    # menyimpan nilai node
        self.left = None    # menyimpan child kiri
        self.right = None   # menyimpan child kanan
        
        
        # membuat traversal postorder
def postorder (node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
        
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

print("Hasil Traversal Postorder : ")
postorder(root)

#penjelasan
'''Disini berlaku "memprioritaskan anak sebelum induk dengan urutan penelusuran kiri-kanan-root.
Alur kerja fungsi postorder() bersifat rekursif dan program akan menyelam hingga ke titik paling bawah di kiri dan 
kanan sebelum mencetak ke node yang sedang dikunjungi. 
Pertama akan dicetak bawah di sisi kiri (D) dan kanan (E) terlebih dahulu sebelum bisa naik ke B.
Begitu pula dengan sisi kanan, di mana F dan G harus
selesai diproses sebelum sampai ke C. Karena semua cabang harus tuntas terlebih dahulu,
maka titik paling atas atau root A akan selalu menjadi data yang paling terakhir muncul'''
