#==========================================================
# Nama : Mouzia Syawalova Merro
# NIM : J0403251080
# Kelas : TPL B2
#==========================================================

#==========================================================
# Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi) 
#==========================================================

#representasi graph menggunakan adjancency list
graph = { 
    'Rumah': ['Sekolah', 'Toko'], 
    'Sekolah': ['Perpustakaan'], 
    'Toko': ['Pasar'], 
    'Perpustakaan': [], 
    'Pasar': [] 
} 

#Graph tersebut menggambarkan jalur dari Rumah ke lokasi lain. Gunakan algoritma 
#BFS untuk menampilkan urutan kunjungan node dimulai dari Rumah. 

from collections import deque

def bfs(graph, start):
    #visited untuk mencatat node yang sudah dikunjungi agar tidak terjadi pengulangan (loop) 
    visited = set() 
    
    #queue adalah tempat menyimpan node yang akan dibaca. Disini dimulasi dengan memasukkan node 'start'
    queue = deque([start]) 
    
    #tandai node pertama sebagai yang sudah dikunjungi
    visited.add(start) 
    
    #selama antrean masih ada isinya, proses terus berlanjut
    while queue: 
        #ambil node dari urutan paling depan (first in first out)
        node = queue.popleft() 
        print(node, end=" ") 
        
        #periksa semua tetangga dari node yang sedang dibaca
        for neighbor in graph[node]: 
            
            #tandai sebagai dikunjungi dan masuk ke antrean untuk diproses nanti
            if neighbor not in visited: 
                visited.add(neighbor)   
                queue.append(neighbor) 
                
print("BFS dari Rumah:") 
bfs(graph, 'Rumah')


#Pertanyaan Analisis
'''1. Node mana yang dikunjungi pertama? 
    Rumah, karena rumah adalah node pertama yang berperan sebagai start.
    
    2. Mengapa BFS cocok untuk mencari jalur terdekat?
    Karena BFS menjelajah secara bertahap atau level by level.
    BFS akan mengunjungi node dengan jalur lebih pendek dahulu.
    
    3. Apa perbedaan urutan BFS jika struktur graph diubah?
    - jika 'Rumah' diubah urutannya menjadi yang lain seperti 'Sekolah' atau 'Toko',
    maka urutan kunjungan node pada level yang sama akan berubah.
    BFS akan mengunjungi 'Toko' dahulu sebelum 'Sekolah'.
    Sehingga, tetangga dari 'Toko' yakni 'Pasar' juga akan dibaca
    lebih dulu daripada tetangga 'Sekolah'.
'''

 