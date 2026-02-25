#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Studi Kasus : Generator PIN
#================================================================

def buat_pin(panjang, hasil=""):
    
    if len(hasil) == panjang:
        print("PIN : ", hasil)
        return
    
    for angka in ["0", "1", "2"]:
        buat_pin(panjang, hasil+angka)
        
buat_pin(3)


     