#==========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
#==========================================================

#==========================================================
# Implementasi DFS
#==========================================================

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
    
}

def dfs(graph, node, visited):
    #Fungsi untuk melakukan penelusuran dengan DFS
    #graph : dictionary yang menyimpan struktur dari graph
    #node : menyimpan node yang sedang dikunjungi 
    #visited : menyimpan node yang sudah dikunjungi 
    
    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)
    
    #tampilkan node yang sedang dikunjungi
    print(node, end=' ')
    
    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        #jika tetangga belum pernah dikunjungi 
        if neighbor not in visited:
            #lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

#set visited
visited = set()
            
#menjalankan dfs dari A
dfs(graph, "A", visited)