#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Materi Rekursif : Faktorial
# Recursive case => 3! = 3 x 2 x 1
# base case => 0 berhenti
#================================================================

def faktorial(n):
    # base case
    # 0! didefinisikan sebagai 1, untuk mencegah fungsi memanggil diri sendiri selamanya
    if n == 0 :
        return 1
    
    #recursive case 
    return n*faktorial(n-1)  # n-1*n-2*n-3.........*n-n

print("==== Program Faktorial ====")       
print("Hasil faktorial : ", faktorial(3))    # memanggil fungsi dengan n = 3