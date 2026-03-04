#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Latihan 1 : Memahami Kode Program (Insertion Sort)
#================================================================

def insertion_sort(data):
    # Loop dimulai dari indeks ke-1 hingga akhir list
    # Anggap elemen pertama (indeks 0) sudah terurut
    for i in range(1, len(data)):
        # key adalah elemen yang akan kita sisipkan ke posisi yang benar
        key = data[i]
        # j adalah indeks elemen di sebelah kiri 'key'
        j = i - 1

        # Geser elemen yang lebih besar dari 'key' ke arah kanan
        # Loop berhenti jika mencapai awal list atau menemukan angka <= key
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]  #menggeser elemen ke kanan
            j -= 1      #berpindah ke indeks sebelumnya di kiri
        # Letakkan key di posisi yang tepat (di depan elemen yang lebih kecil dari nilai key)
        data[j + 1] = key

    return data



'''
Jawaban Soal :
1. Mengapa perulangan dimulai dari indeks 1?
    ==> karena pada program insetion sort, elemen pertama (index 0) dianggap sudah terurut.
        algoritma pada kode ini bekerja dengan cara menganggap bagian kiri sudah sorted(terurut) lalu mengambil elemen berikutnya kemudian menyisipkannya ke posisi yang benar di bagian yang sudah terurut.
        karena jikamulai dari index 0, tidak ada elemen sebelumnya untuk dibandingkan.

2. Apa fungsi variabel key? 
==> Variabel "key" berfungsi untuk menyimpan nilai sementara dari elemen yang akan dipindahkan.
    Saat proses pergeseran terjadi di dalam loop while, nilai pada data[j+1] akan ditimpa oleh nilai yang lebih besar. Tanpa menyimpan nilai tersebut di dalam key, maka akan kehilangan angka yang ingin diurutkan tadi.

3. Mengapa digunakan while, bukan for?
==> while lebih efisien di gunakan pada kode ini karena jumlah pergeserannya yang tak pasti.
    Loop while memungkinkan kita untuk terus bergerak mundur (ke kiri) selama syarat tertentu terpenuhi, yang sulit dilakukan dengan struktur for standar dalam konteks penyisipan ini.

4. Operasi apa yang terjadi di dalam while? 
==> Operasi yang terjadi di dalam while adalah pergeseran (shifting).
    Selama elemen di sebelah kiri (data[j]) lebih besar daripada key, algoritma akan menyalin atau menggeser elemen tersebut satu posisi ke kanan (data[j + 1] = data[j]). Ini dilakukan untuk "membuka ruang" agar key nantinya bisa disisipkan di posisi yang tepat.
'''