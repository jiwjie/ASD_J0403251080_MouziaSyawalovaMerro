#================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# Materi 1 : Dijkstra
#================================================

import heapq 

#Representasi graf menggunakan Adjacency List (Dictionary di dalam Dictionary)

graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
}

def dijkstra(graph, start): 
    # Inisialisasi: Buat tabel jarak semua node menjadi tak terhingga 
    # Ini menandakan bahwa di awal, kita belum tahu jarak ke node-node tersebut.
    distances = {node: float('inf') for node in graph} 
 
    # Jarak ke titik awal diatur menjadi 0
    distances[start] = 0 
 
    # Priority Queue (pq) digunakan untuk mengambil node dengan jarak terkecil berikutnya.
    # Format di dalam list: (jarak_saat_ini, nama_node)
    pq = [(0, start)] 
 
    while pq: 
        # Ambil node dengan jarak terkecil dari priority queue
        current_distance, current_node = heapq.heappop(pq) 
 
        # Jika jarak yang baru diambil lebih besar dari jarak yang sudah tercatat di tabel,
        # maka abaikan (optimasi agar tidak memproses rute yang sudah basi/lebih panjang)
        if current_distance > distances[current_node]: 
            continue 
 
        # Periksa semua tetangga dari node yang sedang diproses
        for neighbor, weight in graph[current_node].items(): 
 
            # Hitung kalkulasi jarak baru
            distance = current_distance + weight 
 
            # Jika rute baru ini lebih kecil (lebih efisien) dari rute yang dicatat sebelumnya
            if distance < distances[neighbor]: 
                # Perbarui tabel jarak minimum
                distances[neighbor] = distance 
 
                # Masukkan ke priority queue untuk mengecek cabang rute selanjutnya
                heapq.heappush(pq, (distance, neighbor)) 
 
    return distances 

# Memanggil fungsi dengan node awal 'A'
hasil = dijkstra(graph, 'A') 

# Menampilkan output akhir berupa dictionary jarak terpendek
print("Jarak terpendek dari A ke setiap node:")
print(hasil)