# ============================================================
# Nama : Mouzia Syawalova Merro 
# NIM : J0403251080
# Kelas : TPL B2
# Praktikum 13 - Graph III: Spanning Tree
# ============================================================

# ============================================================
# Latihan 5 : Tugas Mandiri: Buat Program MST dengan Kasus Baru
# ============================================================

# Data hubungan antar kota 
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Implementasi Algoritma Kruskal
# Urutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []            # List untuk menyimpan jalur MST
total_weight = 0    # Variabel penghitung total bobot
connected = set()   # Set untuk melacak kota yang sudah terhubung

# Menyeleksi edge menggunakan logika Kruskal
for weight, u, v in edges:
    
    # Memilih edge yang tidak membentuk cycle atau mengambil jalur jika salah satu kota belum masuk ke jaringan
    if u not in connected or v not in connected:
        mst.append((u, v, weight))
        total_weight += weight
        
        # Tandai kedua kota sebagai kota yang sudah terhubung
        connected.add(u)
        connected.add(v)

# Output MST
print("===== Jaringan Antar Kota ======")
print("Jalur MST yang terpilih:")
for u, v, w in mst:
    print(f"{u} - {v} (Bobot: {w})")

# Output total bobot minimum
print(f"\nTotal bobot MST = {total_weight}")


# Jawaban Analisis
'''
1. Kasus apa yang dipilih? 
> Kasus Jaringan Jalan Antar Kota

2. Algoritma apa yang digunakan? 
> Algoritma Kruskal dengan cara kerja yakni menggurutkan semua jalur dari bobot terkecil hingga terbesar.
Lalu mengambil satu per satu selagi jalur tidak membuat cycle. 

3. Edge mana saja yang dipilih dalam MST? 
> Bogor ke Depok (bobot 2), Depok ke Jakarta (bobot 3), Depok ke Bandung (bobot 4).

4. Berapa total bobot MST? 
> Total bobot MST adalah 9 
 Penjumlahan dari masing-masing bobot terpilih yakni 2, 3, dan 4. 
 
5. Mengapa edge tertentu tidak dipilih?
> Jalur tidak terpilih : Bogor - Jakarta (bobot 5), Jakarta - Bandung (bobot 6)
> Tidak dipilih karena bobot kedua jalur tersebut lebih besar daripada jalur yang sudah terpilih. 
Jika tetap dipilih pun, akan terbentuk cycle dan melanggar aturan Spanning Tree.
'''
