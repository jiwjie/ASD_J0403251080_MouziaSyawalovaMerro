#================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# Materi 2 : Bellman-Ford
#================================================

# Representasi graph menggunakan Adjacency List
# A -> B (5), A -> C (4), C -> B (-2)
graph = {
    'A': {'B': 5, 'C': 4},   
    'B': {},                 
    'C': {'B': -2}           
}

def bellman_ford(graph, start): 
    # Inisialisasi jarak awal
    # Semua node diset Infinity (tak hingga) agar jarak pertama kali yang ditemukan pasti lebih kecil
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 

    # Proses Relaksasi Utama
    # Dilakukan sebanyak (V - 1) kali. Karena ada 3 node, maka loop berjalan 2 kali.
    # Ini menjamin informasi jarak terpendek menyebar ke seluruh graf.
    for i in range(len(graph) - 1): 
        # Cek setiap node dan tetangganya (setiap sisi/edge)
        for node in graph: 
            for neighbor, weight in graph[node].items(): 
                # Kondisi Relaksasi
                # Jika jarak ke node asal (distances[node]) sudah ditemukan (bukan inf)
                # DAN jarak baru (jarak asal + bobot) lebih kecil dari jarak yang lama
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]: 
                    # Update dengan jarak yang lebih pendek
                    distances[neighbor] = distances[node] + weight 
                    print(f"Iterasi {i+1}: Update jarak ke {neighbor} menjadi {distances[neighbor]}")

    return distances

# Eksekusi dan tampilkan hasil
hasil = bellman_ford(graph, 'A')

print("\nHasil Akhir Jarak Terpendek dari Node A:")
for node, dist in hasil.items():
    print(f"Ke Node {node} = {dist}")