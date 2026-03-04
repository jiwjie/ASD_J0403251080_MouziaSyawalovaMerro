#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 2 : Melengkapi Potongan Kode
#================================================================

def insertion_sort_asc(data):
    # loop mulai dari data ke 2 (indeks array ke 1)
    for i in range(1, len(data)):
        key = data[i]   #simpan nilai yang disisipkan
        j = i - 1        #indeks elemen terakhir di bagian kiri
        
        # geser elemen yang lebih besar dari key ke kanan
        while j >=0 and data[j] > key :
            data[j+1] = data[j]
            j -= 1
            
        # letakkan key di posisi yang benar
        data[j+1] = key

    return data

angka = [2, 45, 22, 9, 15, 37, 3, 10]
print("Hasil sorting (Ascending) : ", insertion_sort_asc(angka))


#=================================================================
# Descending
#=================================================================

def insertion_sort_desc(data):
    # loop mulai dari data ke 2 (indeks array ke 1)
    for i in range(1, len(data)):
        
        key = data[i]      #simpan nilai yang disisipkan
        j = i - 1       #indeks elemen terakhir di bagian kiri
        
    # geser elemen yang lebih kecil dari key ke kanan 
        while j >= 0 and data[j] < key:
            data[j+1] = data[j]
            j -= 1
        
        data[j+1] = key
    return data

angka = [2, 45, 22, 9, 15, 37, 3, 10]
print("Hasil sorting (Descending) : ", insertion_sort_desc(angka))