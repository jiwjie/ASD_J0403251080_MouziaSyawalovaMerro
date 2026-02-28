#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 1 : Rekursi Pangkat
# Tujuan: Memahami base case dan recursive case
#================================================================

def pangkat (a, n):
    
    # base case
    # karena semua angka yang dipangkatkan 0 sama dengan 1,
    # maka saat n adalah 0, proses berhenti dan kembalikan nilai 1
    if n == 0:
        return 1
    
    # recursive case 
    # pola : a^n = a*a(n-1) >> n akan dikurangi 1 setiap kali pemanggilan dilakukan sehingga menyentuh angka 0  
    # eksekusi perkalian a dengan hasil fungsi pangkat itu sendiri akan berulang sampai n mencapai 0
    return a * pangkat(a, n-1)

# menampilkan hasil
print(pangkat(2, 4))           #output = 16



#==============================================================
# Diskusi : alur program serta base case dan recursive call
#==============================================================
''' 
1. pangkat (2,4) -> return 2* pangkat (2,3)  [jeda, tunggu hasil pangkat(2,3)]
2. pangkat (2,3) -> return 2* pangkat (2,2)  [jeda]
3. pangkat (2,2) -> return 2* pangkat (2,1)  [jeda]
4. pangkat (2,1) -> return 2* pangkat (2,0)  [jeda]
5. pangkat (2,0) -> base case, n == 0, return 1

Unwinding :
- Hasil langkah 5 (angka 1) diberikan ke langkah 4: 2*1 = 2
- Hasil langkah 4 (angka 2) diberikan ke langkah 3: 2*2 = 4
- Hasil langkah 3 (angka 4) diberikan ke langkah 2: 2*4 = 8
- Hasil langkah 2 (angka 8) diberikan ke langkah 1: 2*8 = 16
'''
