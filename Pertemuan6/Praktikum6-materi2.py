#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Insertion Sort dengan Tracing
#================================================================

def insertion_sort(data):
    #melihat data awal
    print("Data awal : ", data)
    print("="*50)
    
    # loop mulai dari data ke 2 (indeks array ke 1)
    for i in range(1, len(data)):
        
        key = data[i]   #simpan nilai yang disisipkan
        j = i-1     #indeks elemen terakhir di bagian kiri
        
        print("Iterasi ke-", i)
        print("Nilai key = ", key)
        print("Bagian Kiri (terurut): ", data[:i])
        print("Bagian Kanan (belum terurut) : ", data[i:])        
        
        #proses pergeseran 
        while j>=0 and data[j] > key:
            data[j+1] = data[j]    
            j -= 1
            # sisipkan key ke posisi yang benar
        data[j+1] = key
        
        print("Setelah disisipkan : ", data)
        print("="*50)
        
    return data

angka = [5,2,4,6,1,3]
print("Hasil Sorting : ", insertion_sort(angka))