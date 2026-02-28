#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Contoh Backtracking 1 : kombinasi Biner (n)
#================================================================

def biner(n, hasil=""):
    
    # base case : jika panjang string sudah m, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # recursive case 
    # choose + explore : tambah '0'
    biner (n, hasil+"0")
    
    # choose + explore : tambah '1'
    biner (n, hasil+"1")    # baris di eksekusi setelah semua cabang "0" selesai

# memulai rekursi dengan panjang 3 digit
biner(3)