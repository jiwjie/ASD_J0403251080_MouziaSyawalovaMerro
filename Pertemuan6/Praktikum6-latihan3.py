#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 3 : Tracing Insertion Sort
#================================================================

def insertion_sort (data):
    #melihat data awal 
    print("Data awal : ", data)
    print("="*50)
    
    # loop mulai dari data ke 2 (indeks array ke 1)
    for i in range (1, len(data)):
        
        key = data[i] # simpan nilai yang disisipkan
        j = i-1 # index elemen terakhir
        
        print("Iterasi ke- ", i)
        print("Nilai key = ", key)
        print("Bagian kiri (terurut) : ", data[:i])
        print("Bagian kanan (belum terurut) : ", data[i:])
        
        # proses pergeseran
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
            
        # sisipkan key ke posisi yang benar
        data[j+1] = key
        print("Setelah disisipkan : ", data )
        print("="*50)
        
    return data

angka = [5, 2, 4, 6, 1, 3]
print("Hasil sorting: ", insertion_sort(angka))



'''
Jawaban Soal : 
1.Tuliskan isi list setelah iterasi i = 1.
   Iterasi ke-  1
    Nilai key =  2
    Bagian kiri (terurut) :  [5]
    Bagian kanan (belum terurut) :  [2, 4, 6, 1, 3]
    Isi list setelah iterasi i = 1 :  [2, 5, 4, 6, 1, 3]
    
2.Tuliskan isi list setelah iterasi i = 3.
    Iterasi ke-  3
    Nilai key =  6
    Bagian kiri (terurut) :  [2, 4, 5]
    Bagian kanan (belum terurut) :  [6, 1, 3]
    Isi list setelah iterasi i = 3 :  [2, 4, 5, 6, 1, 3]
    
3.Berapa kali pergeseran terjadi pada iterasi i = 4?
    Sebelum i=4 listnya seperti ini [2, 4, 5, 6, 1, 3] 
    Iterasi i = 4
    Key = 1

    Bandingkan = 
        6 > 1 (geser 1)
        5 > 1 (geser 2)
        4 > 1 (geser 3)
        2 > 1 (geser 4)
        Total pergeseran = 4 kali =>> angka 6, 5, 4, dan 2 semuanya bergeser ke kanan untuk memberi ruang untuk 1
        Setelah disisipkan = [1, 2, 4, 5, 6, 3]
'''