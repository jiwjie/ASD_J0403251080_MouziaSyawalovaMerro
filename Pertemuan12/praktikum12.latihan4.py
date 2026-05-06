#================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# Praktikum 12 - Graph II : Shortest Path
#================================================

# ========================================================== 
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus 
# Algoritma: Dijkstra 
# ========================================================== 

import heapq 

# Graph lokasi kampus 
# Bobot menunjukkan waktu tempuh dalam menit 
graph = { 
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2}, 
    'Perpustakaan': {'Lab': 3}, 
    'Kantin': {'Lab': 4, 'Aula': 7}, 
    'Lab': {'Aula': 1}, 
    'Aula': {} 
} 

def dijkstra(graph, start): 
    distances = {node: float('inf') for node in graph} 
    distances[start] = 0 

    priority_queue = [(0, start)] 
     
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) 
        
        if current_distance > distances[current_node]: 
            continue 

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight 

            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 

    return distances 

hasil = dijkstra(graph, 'Gerbang') 

print("Jarak terpendek dari Gerbang Kampus:") 
for lokasi, jarak in hasil.items(): 
    print(lokasi, "=", jarak, "menit")

#Pertanyaan Analisis
'''
1. Lokasi yang paling dekat dari Gerbang adalah Kantin yakni 2 menit.

2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit.
   Jalur tercepat: Gerbang -> Kantin -> Lab -> Aula = 2 + 4 + 1 = 7 menit.
Karena jalur langsung Gerbang -> Kantin -> Aula totalnya 9 menit.

3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? 
Tidak, karena bisa saja ada jalur lain yang lebih panjang, tetapi total bobot yang lebih kecil.

4. Dijkstra cocok digunakan pada kasus ini karena:
   1) Semua bobot bernilai positif karena satuan waktu tempuh tidak mungkin negatif.
    2) Ingin tau jalur tercepat dari satu titik ke semua titik lain.
'''