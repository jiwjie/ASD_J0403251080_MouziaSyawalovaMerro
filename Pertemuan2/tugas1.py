#==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama  : Mouzia Syawalova Merro
# NIM   : J0403251080
# Kelas : TPL B2
#==========================================================

#----------------------------------------------------------
# Konstanta Nama File
#----------------------------------------------------------

NAMA_FILE  = "stok_barang.txt"

#----------------------------------------------------------
# Fungsi : Membaca data dari file
#----------------------------------------------------------

def baca_stok(NAMA_FILE):
    stock_dict = {}   #inisialisasi data dictionary kosong
    with open ("stok_barang.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()   #menghilangkan karakter baris baru (\n) di akhir kalimat
            
            data_barang = baris.split(",")   #memisahkan string berdasarkan koma menjadi list
            if len(data_barang) != 3:        #jika baris tidak memiliki 3 kolom (kode, nama barang, stok), maka dilewati
                continue
            
            kode, namaBarang, stok = data_barang 
            stok_int = int(stok)    #Konversi stok dari string ke integer agar bisa dihitung
            stock_dict[kode] = {"barang": namaBarang, "stok": stok_int}    #simpan data barang ke nested dictionary dengan key kode
            kode, namaBarang, stok = baris.split(",")   #Melakukan pemecahan ulang
            
            
    return stock_dict

#Memanggil fungsi baca_stok dan menyimpannya ke variabel global
bukaData = baca_stok(NAMA_FILE)



#----------------------------------------------------------
# Fungsi : Menampilkan semua data
#----------------------------------------------------------
def tampilkan_barang(stock_dict):
    
    #Cek apakah dictionary kosong
    if len(stock_dict) == 0 :
        print ("Stok barang kosong.")
        return
    
    #membuat Header Tabel
    print ("\n======= Daftar Stok Barang =======")
    print(f"{'Kode': <10} | {'Barang': <14} | {'Stok': >5}")
    print("-" * 33)    #membuat strip 33 kali (garis header)
    
    #Looping data yang sudah diurutkan berdasarkan key (kode barang)
    for kode in sorted(stock_dict):
        namaBarang = stock_dict[kode]["barang"]
        stok = stock_dict[kode]["stok"]
        print(f"{kode: <10} | {namaBarang: <14} | {stok: >5}")



#----------------------------------------------------------
# Fungsi : Cari barang berdasarkan kode
#----------------------------------------------------------

def cari_barang(stock_dict):
    
    #mencari barang berdasarkan kode barang
    kode_cari = input("Masukkan kode barang yang ingin dicari : ").strip()
    
    #Cek apakah key (kode_cari) ada di dalam dictionary
    if kode_cari in stock_dict:
        namaBarang = stock_dict[kode_cari]["barang"].strip()     #Mengambil data dan melakukan .strip() pada nama barang
        stok = stock_dict[kode_cari]["stok"]
        
        print("\n=== Barang Ditemukan ===")
        print(f"Kode : {kode_cari}")
        print(f"Barang : {namaBarang}")
        print(f"Stok : {stok}")
    
    else:
        print("\nBarang Tidak Ditemukan.")



#----------------------------------------------------------
# Fungsi : Tambah barang baru
#----------------------------------------------------------

def tambah_barang(stock_dict):
    print("\n=== Tambah Barang Baru ===")
    kode = input("Masukkan Kode Barang : ").strip()
    
    #Validasi agar tidak ada kode barang ganda
    if kode in stock_dict:
        print(f"Gagal! Kode {kode} sudah digunakan oleh barang: {stock_dict[kode]['barang']} ")
        
    else:
        #Input nama dan jumlah stok untuk barang baru
        namaBarang = input("Masukkan Nama Barang : ").strip()
        stok = input("Masukkan Jumlah Stok Barang : ").strip()
        
        #Menyimpan data baru ke dictionary
        stock_dict[kode] = {
            "barang" : namaBarang,
            "stok" : stok
        }
        print(f"Berhasil! {namaBarang} telah ditambahkan.")



#----------------------------------------------------------
# Fungsi  : Update Stok Barang
#----------------------------------------------------------

def update_stok(stock_dict):
    
    print("\n==== Update Stock Barang ====")
    
    #cari kode barang yang akan di update jumlah stoknya
    kodeBarang = input("Masukkan kode barang yang ingin diupdate : ").strip()
    
    #Cek keberadaan barang
    if kodeBarang not in stock_dict:
        print ("\nKode Barang tidak ditemukan. Update dibatalkan.")
        return
    
    #Pilih jenis update (apakah dikurangi atau ditambah dari stok tersedia)
    print("Pilih jenis update :")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    
    pilihan = input("Masukkan pilihan (1/2) : ").strip()    
    
    if pilihan not in ["1", "2"] :
        print("Pilihan tidak valid! Update dibatalkan.")
        return
    
    try:
        #Input jumlah perubahan stok
        jumlah = int(input("Masukkan jumlah stok : "))
        
        if jumlah < 0:             #Stok tidak boleh negatif
            print("Jumlah harus berupa angka positif.")
            return
        
        stokLama = stock_dict[kodeBarang]['stok']          #Mengambil nilai stok saat ini sebelum diupdate
        
        #Logika perhitungan
        if pilihan == "1":
            stokBaru = stokLama + jumlah
        elif pilihan == "2":
            #agar stok tidak menjadi minus setelah dikurangi
            if jumlah > stokLama: 
                print(f"Stok tidak mencukupi! Stok saat ini {stokLama}")
            stokBaru = stokLama - jumlah
        
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan.")   #jika user memasukkan karakter selain angka pada input
        return
    
    #menyimpan hasil stok baru ke dictionary
    stock_dict[kodeBarang]["stok"] = stokBaru
    
    print(f"Update berhasil. Stok barang berubah dari {stokLama} menjadi {stokBaru}")



#----------------------------------------------------------
# Fungsi : Menyimpan perubahan ke file
#----------------------------------------------------------

def simpanUpdate(NAMA_FILE, stock_dict):
    with open(NAMA_FILE, "w", encoding="utf-8") as file:
        for kode in sorted(stock_dict.keys()):             #Mengurutkan kode
            namaBarang = stock_dict[kode]["barang"]
            stok = stock_dict[kode]["stok"]
            file.write(f"{kode}, {namaBarang}, {stok}\n")    #Menuliskan kembali data ke file .txt



#----------------------------------------------------------
# Program Utama
#----------------------------------------------------------

def main():

    #Load data awal ke dalam variabel
    bukaData = baca_stok (NAMA_FILE)

    #Perulangan menu agar program terus berjalan sampai user memilih keluar
    while True:
        print("\n=== MENU DATA BARANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        #Mengambil input dari user
        pilih = int(input("Pilihan menu : "))    
        
        # Percabangan untuk memanggil fungsi yang sesuai
        if pilih == 1:
            tampilkan_barang(bukaData)
        elif pilih == 2:
            cari_barang(bukaData)
        elif pilih == 3:
            tambah_barang(bukaData)
        elif pilih == 4:
            update_stok(bukaData)
        elif pilih == 5:
            simpanUpdate(NAMA_FILE, bukaData)
            print("\nUpdate stok berhasil disimpan.")
        elif pilih == 0 :
            print("\nProgram Selesai.")
            break      #Menghentikan loop 
        else: 
            print("\nPilihan tidak valid. Coba lagi.")   #Mengatasi error jika user memasukkan selain angka

            
if __name__ == "__main__":   #memastikan fungsi main() dipanggil
    main()