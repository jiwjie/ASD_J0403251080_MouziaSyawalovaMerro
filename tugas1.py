#==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)

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
    stock_dict = {}
    with open ("stok_barang.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            
            data_barang = baris.split(",")
            if len(data_barang) != 3:
                continue
            
            kode, namaBarang, stok = data_barang 
            stok_int = int(stok)
            stock_dict[kode] = {"barang": namaBarang, "stok": stok_int}
            kode, namaBarang, stok = baris.split(",") 
            
            
    return stock_dict
    
bukaData = baca_stok(NAMA_FILE)

#----------------------------------------------------------
# Fungsi : Menampilkan semua data
#----------------------------------------------------------
def tampilkan_barang(stock_dict):
    
    if len(stock_dict) == 0 :
        print ("Barang Kosong")
        return
    
    print ("\n======= Daftar Stok Barang =======")
    print(f"{'Kode': <10} | {'Barang': <14} | {'Stok': >5}")
    print("-" * 33)
    
    for kode in sorted(stock_dict):
        namaBarang = stock_dict[kode]["barang"]
        stok = stock_dict[kode]["stok"]
        print(f"{kode: <10} | {namaBarang: <14} | {stok: >5}")

#----------------------------------------------------------
# Fungsi : Cari barang berdasarkan kode
#----------------------------------------------------------

def cari_barang(stock_dict):
    
    kode_cari = input("Masukkan kode barang yang ingin dicari : ").strip()
    
    if kode_cari in stock_dict:
        namaBarang = stock_dict[kode_cari]["barang"].strip()
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
    
    if kode in stock_dict:
        print(f"Gagal! Kode {kode} sudah digunakan oleh barang: {stock_dict[kode]['barang']} ")
        
    else:
        namaBarang = input("Masukkan Nama Barang : ").strip()
        stok = input("Masukkan Jumlah Stok Barang : ").strip()
        
        stock_dict[kode] = {
            "barang" : namaBarang,
            "stok" : stok
        }
        print(f"Berhasil! {namaBarang} telah ditambahkan.")

#----------------------------------------------------------
# Fungsi  : Update Stok Barang
#----------------------------------------------------------

def update_stok(stock_dict):
    
    kodeBarang = input("Masukkan kode barang yang ingin diupdate : ").strip()
    
    if kodeBarang not in stock_dict:
        print ("\nKode Barang tidak ditemukan. Update dibatalkan.")
        return
        
    print("Pilih jenis update :")
    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    
    pilihan = input("Masukkan pilihan (1/2) : ").strip()    
    
    if pilihan not in ["1", "2"] :
        print("Pilihan tidak valid! Update dibatalkan.")
        return
    
    try:
        jumlah = int(input("Masukkan jumlah stok : "))
        if jumlah < 0:
            print("Jumlah harus berupa angka positif.")
            return
        
        stokLama = stock_dict[kodeBarang]['stok']
        
        if pilihan == "1":
            stokBaru = stokLama + jumlah
        elif pilihan == "2":
            if jumlah > stokLama: 
                print(f"Stok tidak mencukupi! Stok saat ini {stokLama}")
            stokBaru = stokLama - jumlah
        
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan.")
        return
        
    stock_dict[kodeBarang]["stok"] = stokBaru
    
    print(f"Update berhasil. Stok barang berubah dari {stokLama} menjadi {stokBaru}")

#----------------------------------------------------------
# Fungsi : Menyimpsn perubahan ke file
#----------------------------------------------------------

def simpanUpdate(NAMA_FILE, stock_dict):
    with open(NAMA_FILE, "w", encoding="utf-8") as file:
        for kode in sorted(stock_dict.keys()):
            namaBarang = stock_dict[kode]["barang"]
            stok = stock_dict[kode]["stok"]
            file.write(f"{kode}, {namaBarang}, {stok}\n")

#----------------------------------------------------------
# Program Utama
#----------------------------------------------------------

def main():

    bukaData = baca_stok (NAMA_FILE)

    while True:
        print("\n=== MENU DATA BARANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")
        
        pilih = int(input("Pilihan menu : "))
        
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
            break
        else: 
            print("\nPilihan tidak valid. Coba lagi.")
            
if __name__ == "__main__":
    main()