#================================================================
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#================================================================

#================================================================
# Studi Kasus : Generator PIN
#================================================================

def buat_pin(panjang, hasil=""):
    
    # base case 
    # kombinasi PIN terbentuk ketika panjang teks di 'hasil' sudah sama dengan 'panjang' yang diminta
    if len(hasil) == panjang:
        print("PIN : ", hasil)
        return
    
    # recursive case 
    for angka in ["0", "1", "2"]:
        # memanggil fungsi untuk menentukan digit selanjutnya
        buat_pin(panjang, hasil+angka)

# memanggil fungsi        
buat_pin(3)



#====================================================================
# Diskusi : bagaimana cara mencegah angka yang sama muncul berulang? 
#====================================================================

'''
Untuk mencegah pengulangan elemen, gunakan teknik "Pruning" (pemangkasan)
> caranya dengan menambahkan conditional statement sebelum melakukan pemanggilan rekursif


Prinsip LIFO :

Fase In (Eksplorasi jalur pertama):
1. Eksekusi buat_pin(3, ""): loop mulai dengan "0". panggil buat_pin(3, "0"). pilihan "1" dan "2" ditunda di stack
2. Eksekusi buat_pin(3, "0"): loop mulai dengan "0". panggil buat_pin(3, "00"). pilihan "1" dan "2" ditunda
3. Eksekusi buat_pin(3, "00"): loop mulai dengan "0". panggil buat_pin(3, "000"). Pilihan "1" dan "2" ditunda
4. Eksekusi buat_pin(3, "000"): base case terpenuhi. cetak "PIN : 000", kemudian return

Fase Unwinding & Percabangan (Backtracking):
5. Kontrol kembali ke buat_pin(3, "00"): melanjutkan loop ke angka berikutnya -> panggil buat_pin(3, "001")
6. Eksekusi buat_pin(3, "001"): base case terpenuhi. cetak "PIN : 001", kemudian return
7. Kontrol kembali ke buat_pin(3, "00"): melanjutkan loop ke angka terakhir -> panggil buat_pin(3, "002")
8. Eksekusi buat_pin(3, "002"): base case terpenuhi. cetak "PIN : 002", kemudian return

=====
9. Kontrol kembali ke buat_pin(3, "0"): karena loop "00x" sudah habis, mundur ke level sebelumnya. melanjutkan loop setelah "0" -> panggil buat_pin(3, "01")
10. Proses ini berulang: "01" akan mengeksplorasi "010", "011", "012", dan seterusnya hingga mencapai kombinasi terakhir "222"

Selesai
'''

     