# ========================================================== 
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# ========================================================== 

# ========================================================== 
# Implementasi Kruskal 
# ========================================================== 

# Daftar edge: (bobot, node1, node2) 
edges = [ 
    (1, 'C', 'D'), 
    (2, 'A', 'C'), 
    (3, 'B', 'D'), 
    (4, 'A', 'B'), 
    (5, 'A', 'D') 
]

# Mengurutkan edge berdasarkan bobot 
edges.sort() 
 
mst = []    # List untuk menyimpan jalur MST
total_weight = 0  # Variabel penghitung total bobot
 
# Set sederhana untuk node yang sudah dipilih 
connected = set() 
 
# Menyeleksi edge menggunakan logika Kruskal
for weight, u, v in edges: 
 
    # Jika edge tidak membentuk cycle sederhana atau mengambil jalur jika salah satu node belum terhubung
    if u not in connected or v not in connected: 
 
        mst.append((u, v, weight)) 
        total_weight += weight 

        # Tandai sebagai node yang sudah terhubung
        connected.add(u) 
        connected.add(v) 
 
# Output MST
print("Minimum Spanning Tree:") 
 
for edge in mst: 
    print(edge) 
 
# Ouput total bobot
print("Total bobot =", total_weight)