#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 2 : Tracing Rekursi
# Tujuan : Memahami alur masuk dan keluar fungsi pada proses rekursi
#================================================================

def countdown(n):
    
    # base case
    # jika n mencapai 0, maka akan menampilkan "selesai" dan rekursi berhenti 
    if n == 0:
        print("Selesai")
        return
    
    # saat fungsi dipanggil menuju base case 
    print("Masuk : ", n)
    
    # recursive case 
    countdown (n-1)         # fungsi memanggil dirinya sendiri dengan argumen yang dikurangi 1 (n-1)
    print("Keluar : ", n)       # proses eksekusi terjadi setelah pemanggilan rekursif mencapai base case

# menginisialisasi pemanggilan fungsi
countdown(3)

#====================================================
# Diskusi : Mengapa output 'Keluar' muncul terbalik?
#====================================================
'''
prinsip LIFO (Last In First Out)

Fase In :
1. eksekusi countdown (3): Cetak "Masuk: 3" -> panggil countdown(2). Instruksi cetak "Keluar: 3" ditunda di stack.
2. eksekusi countdown (2): Cetak "Masuk: 2" -> panggil countdown(1). Instruksi cetak "Keluar: 2" ditunda di stack.
3. eksekusi countdown (1): Cetak "Masuk: 1" -> panggil countdown(0). Instruksi cetak "Keluar: 1" ditunda di stack.
4. eksekusi countdown (0): Cetak "Masuk: 0" : base case terpenuhi. Cetak "selesai", kemudian "return"

Fase Unwinding :
5. Kontrol kembali ke countdown(1): Eksekusi sisa instruksi -> cetak "Keluar: 1", selesai
6. Kontrol kembali ke countdown(2): Eksekusi sisa instruksi -> cetak "Keluar: 2", selesai
7. Kontrol kembali ke countdown(3): Eksekusi sisa instruksi -> cetak "Keluar: 3", selesai
'''