#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Contoh Backtracking 2 : Kombinasi Biner dengan Batas '1' (Pruning)
#================================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    
    # Pruning (Pemangkasan): jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas :
        return
    
    # base case
    # jika panjang string 'hasil' sudah sama dengan 'n', cetak
    if len(hasil) == n:
        print(hasil)
        return
    
    # recursive case 
    # Pilih '0'
    biner_batas(n, batas, hasil+"0", jumlah_1)  # saat memilih 0, jumlah_1 tidak bertambah
    
    # Pilih '1'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)    # jika memilih '1', tambahkan jumlah_1 dengan 1
    
# memanggil fungsi 
biner_batas(4,2)