# ========================================================== 
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# ========================================================== 

# ========================================================== 
# Implementasi Prim 
# ========================================================== 


import heapq 
 
# Daftar edge dan bobot ke masing-masing vertex
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 
 
def prim(graph, start): 
    # Set untuk mencatat node mana saja yang sudah dikunjungi
    visited = set([start]) 
 
    # Menyimpan edge yang akan dipilih 
    edges = [] 
    
    # Memasukkan semua tetangga dari titik awal ke dalam heap 
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    
    # List menyimpan jalur yang terpilih
    mst = [] 
    
    # Variabel untuk menghitung total bobot MST
    total_weight = 0 
 
    # Perulangan jika masih ada edge dalam heap 
    while edges: 
        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges) 

        # Cek jika node tujuan belum dikunjungi 
        if v not in visited: 
            # Tandai sudah dikunjungi
            visited.add(v) 
 
            # Menambah edge ke list MST dan menambah bobot
            mst.append((u, v, weight)) 
            total_weight += weight 
 
            # Menambah node baru ke dalam heap
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
 
    return mst, total_weight 
 
 # Menjalankan fungsi prim
mst, total = prim(graph, 'A') 
# Menampilkan hasil
print("Minimum Spanning Tree:") 
for edge in mst: 
    print(edge) 
print("Total bobot =", total)