# ============================================================
# Nama : Mouzia Syawalova Merro 
# NIM : J0403251080
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ============================================================

# ============================================================
# Latihan 2 : Implementasi Sederhana Algoritma Kruskal
# ============================================================

# Daftar edge 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
] 
# Mengurutkan edge berdasarkan bobot terkecil 
edges.sort() 

mst = []            # List untuk menyimpan jalur MST
total_weight = 0     # Variabel untuk menghitung total bobot
connected = set()   # Set untuk melacak node yang sudah terhubung

# Menyeleksi edge
for weight, u, v in edges: 
    
    # Memilih edge yang tidak membentuk cycle atau mengambil jalur jika salah satu node belum terhubung
    if u not in connected or v not in connected: 
        mst.append((u, v, weight)) 
        total_weight += weight 
        
        # Tandai sudah terhubung
        connected.add(u) 
        connected.add(v) 

# Output MST       
print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 

# Output total bobot 
print("Total bobot =", total_weight)


#Jawaban Analisis 
'''
1. Edge mana yang dipilih pertama kali? 
> edge antara C dan D dengan bobot 1 karena bobotnya yang paling kecil 
dibandingkan edge lain.

2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu? 
> Karena tujuan dari MST yaitu menghubungkan semua node dengan total paling minimum.
Jadi ketika memilih bobot terkecil dahulu, total keseluruhan akan lebih kecil nantinya 
(misal total biaya / jarak).

3. Berapa total bobot MST yang dihasilkan?
>  Total bobot MST adalah 6. Nilai tersebut didapat dari penjumlahan edge yakni 1,2, dan 3.

4. Mengapa edge tertentu tidak dipilih? 
> Karena semua node terhubung sudah memiliki bobot terkecil. Jika edge lain tetap ditambah/dipilih, 
maka total bobot akan membesar dan terbentuk cycle. 
'''
