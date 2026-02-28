#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# Masuk 1 - 2 - 3 
# Keluar 
#================================================================

def hitung(n):
    
    #base case
    # jika n mencapai 0, cetak "selesai" dan berhenti
    if n == 0:
        print("Selesai")
        return
    
    # eksekusi berjalan ketika fungsi menuju base case
    print("Masuk : ", n)
    
    #recursive case 
    # memanggil diri sendiri 
    hitung(n-1)     
    print("Keluar : ", n)       #baris ini akan dijeda sampai proses diatasnya selesai
    
print("==== Program Tracing ====")
hitung(3)       #menghitung program dengan angka 3