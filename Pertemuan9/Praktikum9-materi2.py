#=================================================
#Nama: Mouzia Syawalova Merro
#NIM : J0403251080
#Kelas : TPL B-B2
#=================================================

#=================================================
#Latihan 2: Membuat Binary Search Tree Sederhana
#=================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data    #menyimpan nilai node
        self.left = None    #child kiri
        self.right = None   #child kanan

#membuat sebuah node root
root = Node("A") 

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

#menampilkan isi node
print("Data pada root", root.data)
print("Child kiri root", root.left.data)
print("Child kanan root", root.right.data)
print("Child kiri dari B: ", root.left.left.data)
print("Child kanan dari B: ", root.left.right.data)
print("Child kiri dari C: ", root.right.left.data)
print("Child kanan dari C: ", root.right.right.data)

#penjelasan
'''Kode ini menunjukkan cara merangkai node yang semula berdiri sendiri menjadi stuktur pohon yang bertingkat.
Alur kode ini dimulai dengan membuat root yang berisi nilai "A". 
Setelah itu, dibentuk dua cabang dibawahnya yakni bernilai "B" di kiri dan "C" di kanan.
Kemudian, pada cabang "B" diberikan dua cabang lagi yaitu "D" di kiri dan "E"di kanan. 
Sedangkan untuk "C", terdapat cabang "F" di kiri dan "G" kanan. 
Disinilah terbentuk sebuah pohon/tree yang bisa kita lakukan pemanggilan dengan 3 cara yang telah dipelajari.'''