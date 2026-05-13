# ============================================================
# Nama : Mouzia Syawalova Merro 
# NIM : J0403251080
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ============================================================

# ============================================================
# Latihan 3 : Implementasi Algoritma Prim
# ============================================================

import heapq 

# Data hubungan antar node 
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

def prim(graph, start): 
    # Set untuk melihat node yang sudah dikunjungi 
    visited = set([start]) 
    edges = []  # menyimpan edge 
    
    # memasukkan tetangga node awal ke heap
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 
    
    # menyimpan edge MST dan variabel total bobot
    mst = [] 
    total_weight = 0 
    
    # perulangan selama edge masih bisa dieksplor
    while edges:
        # mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges) 
        
        # mengecek apakah node belum pernah dikunjungi 
        if v not in visited: 
            # menandai node sudah dikunjungi
            visited.add(v) 

            # memasukkan edge terpilih ke MST dan menambah bobot
            mst.append((u, v, weight)) 
            total_weight += weight 
            
            # mengecek tetangga node baru dikunjungi untuk masuk ke heap
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 
    
    return mst, total_weight 

# menjalankan dari node A
mst, total = prim(graph, 'A') 

# output MST
print("Minimum Spanning Tree:") 

for edge in mst: 
    print(edge) 

# output total bobot
print("Total bobot =", total)


# Jawaban Analisis 
'''
1. Node awal apa yang digunakan? 
> Node A

2. Edge mana yang dipilih pertama kali? 
> Edge A lalu ke C dengan bobot 2

3. Bagaimana Prim menentukan edge berikutnya? 
> Memilih edge dengan bobot terkecil yang menghubungkan node yang sudah
dan belum dikunjungi. 

4. Berapa total bobot MST yang dihasilkan?
> A - C = 2
  C - D = 1
  D - B = 3
  total = 6
   
5. Apa perbedaan pendekatan Prim dan Kruskal?
> Prim dimulai dari satu titik ke titik terdekat dengan bobot terkecil. Hal itu dilakukan 
sampai semua terhubung. 
Sedangkan kruskal mengurutkan semua edge dari terkecil dan diambil satu persatu selama tidak
terbentuk cycle.
'''
