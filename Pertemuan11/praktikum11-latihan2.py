#==========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
#==========================================================

#==========================================================
# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur) 
#==========================================================

#representasi graph menggunakan adjancency list
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': [], 
    'F': [] 
} 

def dfs(graph, node, visited): 
    # tandai node saat ini sebagai sudah dikunjungi
    visited.add(node) 
    
    # tampilkan node yang sedang dikunjungi dengan format panah ->
    print(node, end=" -> ") 
    
    # periksa semua tetangga dari node saat ini
    for neighbor in graph[node]: 
        
        # jika tetangga belum pernah dikunjungi
        if neighbor not in visited: 
            # lakukan DFS secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited) 
            
# inisialisasi set kosong untuk menyimpan node yang sudah dikunjungi 
visited = set() 

print("DFS dari A:") 
dfs(graph, 'A', visited)
print("Proses selesai")


#Pertanyaan Analisis
'''
1.  Mengapa DFS masuk ke node terdalam terlebih dahulu?
    Karena prinsip rekursif yang bekerja seperti struktur data stack (LIFO).
    Saat ada tetangga baru, eksekusi saat ini tertunda sementara. Lanjut, fungsi akan
    memanggil dirinya sendiri untuk menelusuri tetangga baru tadi. 
    Penelurusan lanjut terus hingga bawah cabang sampai buntu. Terakhir, 
    akan dilakukan backtrack ke node sebelumnya.
    
2. Apa yang terjadi jika urutan neighbor diubah?
    Jalur yang dieksplorasi ikut berubah, karena pemanggilan rekursif berubah urutannya.
    Jika adjacency list 'A' berubah menjadi ['C', 'B'], 'C' lebih dulu dipanggil.
    DFS akan menelusuri seluruh cabang 'C' sampai ke ujung (F), baru backtrack ke cabang 'B'.
    
3. Bandingkan hasil DFS dengan BFS pada graph yang sama
    - Output DFS: A -> B -> D -> E -> C -> F -> Selesai. 
    Eksekusi menelusuri : vertikal/mendalam.
    Jalur kiri dihabiskan dulu (A-B-D), mundur ke B, pindah ke cabang E, mundur hingga ke A, lalu menyelesaikan jalur kanan (C-F).
    
    - Output BFS: A -> B -> C -> D -> E -> F -> Selesai. 
    Eksekusi menelusuri : horizontal/melebar per level. 
    Node diproses tergantung tingkat dekatnya dengan titik awal.
'''
