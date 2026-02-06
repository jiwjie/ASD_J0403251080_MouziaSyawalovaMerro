#==========================================================
# TUGAS 1
#==========================================================

isi_gudang  = "stokBarang.txt"

#Membaca data
def baca_stok_barang(isi_gudang):
    data_dict = {}
    with open ("stokBarang.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            
            data_barang = baris.split(",")
            if len(data_barang) != 3:
                continue
            
            kode, barang, stok = data_barang 
            stok_int = int(stok)
            data_dict[kode] = {"Barang": barang, "Stok": stok_int}
            kode, barang, stok = baris.split(",") 
            
            
    return data_dict
    
bukaData = baca_stok_barang(isi_gudang)
#print("Jumlah data tersedia : ", len(buka_data))


#Tampilkan data
def tampilkan_barang(data_dict):
    
    if len(data_dict) == 0 :
        print ("Barang Kosong")
        return
    
    print ("\n===== Daftar Stok Barang =====")
    print(f"{'Kode': <10} | {'Barang': <12} | {'Stok': >5}")
    print("-" * 33)
    
    for kode in sorted(data_dict):
        barang = data_dict[kode]["barang"]
        stok = data_dict[kode]["stok"]
        print(f"{kode: <10} | {barang: <12} | {stok: >5}")
        
        
#tampilkan_data(buka_data)

#Cari barang berdasarkan kode
def cari_barang(data_dict):
    
    kode_cari = input("Masukkan kode barang yang ingin dicari : ").strip()
    
    if kode_cari in data_dict:
        barang = data_dict[kode_cari]["barang"]
        stok = data_dict[kode_cari]["stok"]
        
        print("\n=== Barang Ditemukan ===")
        print(f"Kode : {kode_cari}")
        print(f"Barang : {barang}")
        print(f"Stok : {stok}")
    
    else:
        print("\nBarang Tidak Ditemukan.")
        
#cari_barang(buka_data)

#Tambah barang baru
def barangBaru(data_dict):
    print("\n=== Tambah Barang Baru ===")
    kode = input("Masukkan Kode Barang : ")
    
    if kode in data_dict:
        print(f"Gagal! Kode {kode} sudah digunakan oleh barang: {data_dict[kode]['barang']} ")
        
    else:
        barang = input("Masukkan Nama Barang : ").strip()
        stok = input("Masukkan Jumlah Stok Barang : ").strip()
        
        data_dict[kode] = {
            "barang" : barang,
            "stok" : stok
        }
        print(f"Berhasil! Barang {barang} telah ditambahkan.")
        
#barangBaru(buka_data)

#Update Stok Barang

def update_stok(data_dict):
    
    kodeBarang = input("Masukkan kode barang yang ingin diupdate : ").strip()
    
    if kodeBarang not in data_dict:
        print ("\nKode Barang tidak ditemukan. Update dibatalkan.")
        return

    try:
        stokBaru = int(input("Masukkan stok baru barang : "))
        
    except ValueError:
        print("Stok harus berupa angka. Update dibatalkan.")
        return
    
    if stokBaru < 0 :
        print("Stok harus berupa angka positif. Update dibatalkan")
        
    stokLama = data_dict[kodeBarang]["stok"]
    data_dict[kodeBarang]["stok"] = stokBaru
    
    print(f"Update berhasil. Stok barang berubah dari {stokLama} menjadi {stokBaru}")

#update_stok(buka_data) 

#Simpan perubahan ke file

def simpanUpdate(isi_gudang, data_dict):
    with open(isi_gudang, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            barang = data_dict[kode]["barang"]
            stok = data_dict[kode]["stok"]
            file.write(f"{kode}, {barang}, {stok}\n")
            
#simpanUpdate(isi_gudang, bukaData)
#print("Update berhasil disimpan")


#Buat menu
def main():

    bukaData = baca_stok_barang (isi_gudang)

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
            barangBaru(bukaData)
            print('\nBarang berhasil ditambahkan.')
        elif pilih == 4:
            update_stok(bukaData)
            print("\nStok barang berhasil diupdate.")
        elif pilih == 5:
            simpanUpdate(isi_gudang, bukaData)
            print("\nUpdate stok berhasil disimpan.")
        elif pilih == 0 :
            print("\nProgram Selesai.")
            break
        else: 
            print("\nPilihan tidak valid. Coba lagi.")
            
if __name__ == "__main__":
    main()