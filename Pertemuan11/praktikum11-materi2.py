#==========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
#==========================================================

#==========================================================
# Implementasi BFS
#==========================================================

#struktur data untuk membuat antrian, gunakan dari library collection
from collections import deque

#representasi graph
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
    
}

def bfs(graph, start):
    #Fungsi untuk melakukan penelusuran dengan BFS
    # graph : dictionary yang menyimpan struktur dari graph
    # start : node awal penelusuran
    
    #queue digunakan untuk menyimpan node yang akan diproses/dibaca
    queue = deque()
    
    #variabel visited : menyimpan node yang sudah diproses/dibaca
    visited = set()
    
    #masukkan node awal ke queue 
    queue.append(start)
    
    #tandai node awal yang sudah masuk queue sebagai node yang sudah dikunjungi
    visited.add(start)
    
    while queue:
        # mengambil node paling depan dari queue
        node = queue.popleft()
        #Tampilkan node yang sedang dikunjungi
        print(node, end='' )
        
        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #masukkan tetangga ke queue untuk diproses
                queue.append(neighbor)
                
# menjalankan BFS dari node A
bfs(graph, 'A')