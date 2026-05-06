#================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# Praktikum 12 - Graph II : Shortest Path
#================================================

# ========================================================== 
# Latihan 2: Implementasi Dijkstra
# ========================================================== 

import heapq 
# Weighted graph dengan bobot positif 
graph = { 
    'A': {'B': 4, 'C': 2}, 
    'B': {'D': 5}, 
    'C': {'D': 1}, 
    'D': {} 
} 
def dijkstra(graph, start): 
    """ 
    Fungsi untuk mencari jarak terpendek dari node start 
    ke seluruh node lain menggunakan algoritma Dijkstra. 
    """
     
    # Semua jarak awal dibuat tak hingga 
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari start ke start adalah 0 
    distances[start] = 0 
    
    # Priority queue menyimpan pasangan (jarak, node) 
    priority_queue = [(0, start)]
    
    while priority_queue: 
        current_distance, current_node = heapq.heappop(priority_queue) 
 
        # Jika jarak saat ini lebih besar dari jarak yang sudah tercatat, 
        # maka proses dilewati 
        if current_distance > distances[current_node]: 
            continue 
 
        # Periksa semua tetangga dari node saat ini 
        for neighbor, weight in graph[current_node].items(): 
            distance = current_distance + weight 
 
            # Jika ditemukan jarak yang lebih kecil, perbarui jaraknya 
            if distance < distances[neighbor]: 
                distances[neighbor] = distance 
                heapq.heappush(priority_queue, (distance, neighbor)) 
 
    return distances 
 
 
hasil = dijkstra(graph, 'A') 
 
print("Jarak terpendek dari node A:") 
for node, distance in hasil.items(): 
    print(node, "=", distance)
    
    

# Pertanyaan Analisis 
'''
1. Berapa jarak terpendek dari A ke B?
    > 4

2. Berapa jarak terpendek dari A ke C? 
    > 2

3. Berapa jarak terpendek dari A ke D? 
    > 3

4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B? 
    > Karena jika melalui B, total bobotnya 9. Sedangkan melalui C, hanya memiliki
    total bobot 3.

5. Apa fungsi priority_queue dalam algoritma Dijkstra? 
    > Untuk memilih node yang lebih efisien. Jadi jalur yang terpilih akan berada pada jalur terpendek.
    Sehingga bisa mengurangi jumlah komputasi yang tidak perlu.

6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?
    > Dijkstra bekerja dengan prinsip: sekali ketemu jalan terpendek, jalan itu tidak akan berubah. 
    Tapi kalau ada bobot negatif, prinsip ini rusak. Karena angka negatif bisa membuat total jarak 
    yang tadinya besar tiba-tiba jadi sangat kecil, dan Dijkstra terlanjur melewatkan jalur tersebut. 
'''
