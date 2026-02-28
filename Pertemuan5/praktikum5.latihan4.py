#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 4 : Kombinasi Huruf
#================================================================

def kombinasi(n, hasil=""):
    
    # base case
    # jika panjang 'hasil' sudah sama dengan n, maka hasilnya akan tercetak dan proses terhenti
    if len(hasil) == n:
        print(hasil)
        return
    
    # recursive case
    # 1. mencoba menambahkan huruf "A" ke kombinasi sekarang dan loncat untuk mengisi posisi karakter sebelumnya
    kombinasi(n, hasil +"A")
    
    # 2. baris ini dieksekusi setelah semua kemungkinan dari "A" selesai, dan lompat lagi untuk mengisi posisi berikutnya
    kombinasi(n, hasil + "B")
    
# memanggil fungsi untuk membuat kombinasi 2 karakter
kombinasi(2)


#==========================================================
# Diskusi : bagaimana jumlah kombinasi yang dihasilkan.
#==========================================================

'''
Jumlah kombinasi mengikuti rumus perpangkatan r^n (r = jumlah opsi, n = panjang)
Dengan 2 opsi karakter ('A', 'B') dan n=2, maka total node yang terbentuk adalah 2^2 = 4 kombinasi (AA, AB, BA, BB)


Fase In (Eksplorasi Cabang Kiri):
1. Eksekusi kombinasi(2, hasil=""): panggil kombinasi(2, "A"). instruksi panggil kombinasi(2, "B") ditunda di stack
2. Eksekusi kombinasi(2, "A"): panggil kombinasi(2, "AA"). instruksi panggil kombinasi(2, "AB") ditunda di stack
3. Eksekusi kombinasi(2, "AA"): base case terpenuhi (len == 2). cetak "AA", kemudian return

Fase Unwinding & In (Backtracking):
4. Kontrol kembali ke kombinasi(2, "A"): melanjutkan sisa instruksi yang ditunda -> panggil kombinasi(2, "AB")
5. Eksekusi kombinasi(2, "AB"): base case terpenuhi. cetak "AB", kemudian return
6. Kontrol kembali ke kombinasi(2, ""): cabang "A" selesai. melanjutkan sisa instruksi yang ditunda -> panggil kombinasi(2, "B")

Fase In Kembali (Eksplorasi Cabang Kanan):
7. Eksekusi kombinasi(2, "B"): panggil kombinasi(2, "BA"). instruksi panggil kombinasi(2, "BB") ditunda di stack
8. Eksekusi kombinasi(2, "BA"): base case terpenuhi. cetak "BA", kemudian return
9. Kontrol kembali ke kombinasi(2, "B"): melanjutkan sisa instruksi yang ditunda -> panggil kombinasi(2, "BB")
10. Eksekusi kombinasi(2, "BB"): base case terpenuhi. cetak "BB", kemudian return

Selesai
'''