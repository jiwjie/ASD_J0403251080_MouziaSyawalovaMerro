# ============================================================
# Nama : Mouzia Syawalova Merro 
# NIM : J0403251080
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ============================================================

# ============================================================
# Latihan 4 : Studi Kasus : Jaringan Kabel Antar Gedung
# ============================================================

import heapq 

# Data hubungan antar gedung 
graph = { 
    'A': {'B': 4, 'C': 2, 'D': 5}, 
    'B': {'A': 4, 'D': 3}, 
    'C': {'A': 2, 'D': 1}, 
    'D': {'A': 5, 'B': 3, 'C': 1} 
} 

# Implementasi Algoritma Prim
def prim(graph, start): 
    # Set untuk melacak gedung yang sudah terhubung kabel
    visited = set([start]) 
    
    # Menyimpan jalur kabel yang akan dilewati
    edges = [] 

    # Masukkan semua jalur dari gedung awal ke dalam heap
    for neighbor, weight in graph[start].items(): 
        heapq.heappush(edges, (weight, start, neighbor)) 

    mst_edges = []      # List untuk menyimpan jalur kabel terpilih
    min_cost = 0        # Variabel untuk menyimpan total biaya

    # Pencarian jalur untuk nilai minimum
    while edges: 
        # Ambil jalur dengan biaya paling murah
        weight, u, v = heapq.heappop(edges) 

        # Jika gedung belum terhubung kabel
        if v not in visited: 
            visited.add(v) 
            mst_edges.append((u, v, weight)) 
            min_cost += weight 

            # Tambahkan jalur baru dari gedung yang baru terhubung
            for neighbor, w in graph[v].items(): 
                if neighbor not in visited: 
                    heapq.heappush(edges, (w, v, neighbor)) 

    return mst_edges, min_cost 

# Eksekusi program dari Gedung A
selected_edges, total_cost = prim(graph, 'A') 

# Output edge yang dipilih
print("====== Jaringan Kabel Antar Gedung =======")
print("Jaringan kabel yang terpilih :") 
for edge in selected_edges: 
    print(f"{edge[0]} - {edge[1]} dengan biaya {edge[2]}") 

# Output total biaya minimum
print("\nTotal biaya minimum pemasangan kabel =", total_cost)


# Jawaban Analisis
'''
1. Algoritma apa yang digunakan? 
> Algoritma prim dengan cara kerja memilih titik awal dan menentukan jalur dengan bobot termurah.

2. Edge mana saja yang dipilih? 
> Jalur dari gedung A ke C (bobot 2), lanjut ke gedung D (bobot 1), terakhir ke gedung B (bobot 3).
 
3. Berapa total biaya minimum? 
> Total biaya minimum adalah 6

4. Mengapa MST cocok digunakan pada kasus ini?
> Karena kasus ini ingin menghubungkan kabel ke seluruh gedung namun mencari biaya pemasangan terendah tanpa 
membuat jalur ganda, yang mana sangat cocok dengan konsep MST.
'''