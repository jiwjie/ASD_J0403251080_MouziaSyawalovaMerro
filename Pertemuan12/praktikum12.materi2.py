#================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# Materi 2 : Bellman Ford
#===============================================

# Representasi graph sesuai gambar
graph = {
    'A': {'B': 5, 'C': 4},   
    'B': {},                 
    'C': {'B': -2}           
}


def bellman_ford(graph, start): 

    # Inisialisasi jarak semua node ke tak hingga 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 
 
    # Relaksasi berulang 
    for _ in range(len(graph) - 1): 
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
                #Jika jarak node asal bukan tak hingga dan ditemukan jalur lebih pendek
                if distances[node] + weight < distances[neighbor]: 
                    distances[neighbor] = distances[node] + weight 
 
    return distances

hasil = bellman_ford(graph, 'A')
print(hasil)    #tampilkan output