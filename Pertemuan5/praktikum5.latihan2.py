#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 2 : Tracing Rekursi
#================================================================

def countdown(n):
    
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk : ", n)
    
    countdown (n-1)
    print("Keluar : ", n)
    
countdown(3)