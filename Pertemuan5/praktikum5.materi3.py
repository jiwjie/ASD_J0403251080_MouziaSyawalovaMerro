#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Materi Rekursif : Menjumlahkan Elemen List
#================================================================

def jumlah_list(data, index=0):
    
    #base case
    # jika indeks sudah sama dengan panjang data, maka dikembalikan ke 0
    if index == len(data):
        return 0
    
    #recursive case
    # angka di posisi indeks sekarang ditambahkan dengan hasil pemanggilan fungsi untuk indeks berikutnya
    return data[index] + jumlah_list(data, index+1)

print("==== Program Jumlah Data List ====")
print(jumlah_list([2,4,5]))     # memanggil fungsi