#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 3 : Mencari Nilai Maksimum
# Tujuan: Mengolah struktur data menggunakan rekursi
#================================================================

def cari_maks(data, index=0):
    
    # base case
    # jika indeks sudah sampai di angka terakhir list, kembalikan angka itu sendiri
    if index == len(data) - 1:
        return data[index]
    
    # recursive case 
    # fungsi memanggil diri sendiri dengan menggeser pointer 'indeks' ke kanan untuk mencari nilai maks pada sisa elemen di list
    maks_sisa = cari_maks(data, index + 1)
    
    # membandingkan angka di posisi sekarang dengan angka terbesar
    if data[index] > maks_sisa:
        # mengembalikan elemen saat ini jika angka lebih besar
        return data[index]
    
    # jika tidak, mempertahankan nilai maksimum dari elemen sebelumnya
    else:
        return maks_sisa

# contoh penggunaan dengan memberikan value dan menampilkan hasil
angka = [3,7,2,9,5]
print("Nilai maksimum : ", cari_maks(angka))



#============================================================
# Diskusi : alur program serta base case dan recursive call
#============================================================
'''
Prinsip LIFO (Last In First Out) :

Fase In :
1. Eksekusi cari_maks(index 0): nilai 3. panggil cari_maks(index 1). perbandingan "3 > a" ditunda di stack >>> a : karena sedang menunggu jawaban jadi belum pasti angka pembandingnya 
2. Eksekusi cari_maks(index 1): nilai 7. panggil cari_maks(index 2). perbandingan "7 > a" ditunda di stack
3. Eksekusi cari_maks(index 2): nilai 2. panggil cari_maks(index 3). perbandingan "2 > a" ditunda di stack
4. Eksekusi cari_maks(index 3): nilai 9. panggil cari_maks(index 4). perbandingan "9 > a" ditunda di stack
5. Eksekusi cari_maks(index 4): nilai 5. base case terpenuhi (indeks terakhir). return nilai 5

Fase Unwinding :
6. Kontrol kembali ke index 3: bandingkan 9 dengan 5 (hasil return). 9 lebih besar. return 9
7. Kontrol kembali ke index 2: bandingkan 2 dengan 9. 9 lebih besar. return 9
8. Kontrol kembali ke index 1: bandingkan 7 dengan 9. 9 lebih besar. return 9
9. Kontrol kembali ke index 0: bandingkan 3 dengan 9. 9 lebih besar. return 9
'''