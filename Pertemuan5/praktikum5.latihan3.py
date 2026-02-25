#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 3 : Mencari Nilai Maksimum
#================================================================

def cari_maks(data, index=0):
    
    # base case
    if index == len(data) - 1:
        return data[index]
    
    # recursive case 
    maks_sisa = cari_maks(data, index + 1)
    
    if data[index] > maks_sisa:
        return data[index]
    
    else:
        return maks_sisa
    
angka = [3,7,2,9,5]
print("Nilai maksimum : ", cari_maks(angka))