#================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
# Praktikum 12 - Graph II : Shortest Path
#================================================

# ========================================================== 
# Latihan 5: Studi Kasus Shortest Path 
# ========================================================== 
import heapq

# Representasi graph berbobot menggunakan dictionary
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Jakarta': {'Bandung': 7},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Bandung': {}
}

def dijkstra(graph, start):
    """
    Fungsi untuk menghitung jalur terpendek menggunakan Algoritma Dijkstra.
    """
    # Inisialisasi semua kota memiliki jarak tak hingga di awal
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari titik mulai ke diri sendiri adalah 0
    distances[start] = 0
    
    # Priority Queue untuk menyimpan pasangan (jarak, nama_kota)
    # heapq akan selalu memberikan kota dengan jarak terkecil
    pq = [(0, start)]
    
    while pq:
        # Pilih kota dengan jarak akumulasi terkecil saat ini
        current_distance, current_city = heapq.heappop(pq)
        
        # abaikan jarak yang saat ini jika lebih besar 
        if current_distance > distances[current_city]:
            continue
            
        # Periksa semua tetangga dari kota saat ini
        for neighbor, weight in graph[current_city].items():
            # Hitung total jarak baru
            distance = current_distance + weight
            
            # Jika rute baru ini lebih efisien
            if distance < distances[neighbor]:
                # Update tabel jarak terpendek
                distances[neighbor] = distance
                # Masukkan ke queue untuk dieksplorasi lebih lanjut
                heapq.heappush(pq, (distance, neighbor))
                
    return distances

# Penentuan node awal (Bogor)
kota_asal = 'Bogor'
hasil_jalur = dijkstra(graph, kota_asal)

# Output jarak terpendek ke semua node
print(f"--- Hasil Jalur Terpendek dari {kota_asal} ---")
for kota, jarak in hasil_jalur.items():
    if jarak == float('inf'):
        print(f"Ke {kota}: Tidak dapat dijangkau")
    else:
        print(f"Ke {kota}: {jarak} km")
        

# Jawaban Analisis: 
'''
1. Node awal yang digunakan apa? 
    > Bogor
2. Node mana yang memiliki jarak paling kecil dari node awal? 
    > Depok
3. Node mana yang memiliki jarak paling besar dari node awal? 
    > Bandung
4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
    > Awalnya algoritma mencatat jarak Bogor yakni 0, dan kota lain dianggap infinity.
    Dari Bogor ada pilihan ke Depok (2) dan Jakarta (5). Dipilih Depok karena jaraknya lebih kecil.
    Dari Depok, baru melihat ke Jakarta. Jarak baru ke Jakarta adalah 4 yakni 2 (ke Depok) + 2 (ke Jakarta).
    Karena jarak langsung ke Jakarta dari Bogor lebih besar, yakni 5, maka jarak ke Jakarta diperbarui jadi 4.
    Lanjut, satu-satunya jalan adalah Bandung dengan bobot 7. Total bobot kita 11.
    Selain itu, di cek juga jalur Depok langsung ke Bandung memiliki bobot 8. Algoritma tetap mencari angka terkecil.
    Setelah semua kota dikunjungi dan tidak ada rute yang lebih pendek lagi, maka itulah hasil akhir jarak paling efisien.
'''