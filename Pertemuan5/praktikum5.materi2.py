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
    
    #base case:
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk : ", n)
    hitung(n-1) #recursive case 
    print("Keluar : ", n)
    
print("==== Program Tracing ====")
hitung(3)