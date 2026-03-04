#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 5 : Melengkapi Fungsi Merge
#================================================================


def merge(left, right):
    result = []
    i = 0
    j = 0 

    # Bandingkan elemen kiri dan kanan selama keduanya masih ada isi
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:                 # Ambil nilai yang lebih kecil (ascending)
            result.append(left[i])              # Masukkan ke result
            i += 1                              # Geser pointer ke kiri
        else:
            result.append(right[j])             # Masukkan ke result 
            j += 1                              # Geser pointer ke kanan

    # Jika masih ada sisa elemen di kiri, tambahkan semua
    result.extend(left[i:])

    # Jika masih ada sisa elemen di kanan, tambahkan semua
    result.extend(right[j:])

    return result 

# ====================
# Panggil Program 
# ====================

left = [8, 14, 5]
right = [1, 7, 10, 45, 15]
hasil = merge(left, right)
print("Hasil Sorting: ", hasil)


"""
Jawaban soal : --> Jelaskan fungsi result.extend()!

==> fungsi result.extend() berguna untuk menambahkan sisa elemen yang belum diproses ke dalam list result.
Hal ini dilakukan agar semua elemen tetap masuk ke hasil akhir setelah proses perbandingan selesai.


Pada proses merge, perbandingan akan terus terjadi selama kedua list masih memiliki elemen. Tapi, sering salah satu list lebih dulu habis. 
jadi, elemen yang masih tersisa harus tetap dimasukkan agar tidak hilang.

Metode extend() menambahkan seluruh elemen yang tersisa sekaligus ke dalam list result. 
extend() akan menambahkan semua isi list yang diberikan. 
Jadi, result.extend() memastikan seluruh data ada dengan lengkap dan dalam urutan yang benar.
"""