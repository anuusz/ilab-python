# Program ini menghitung rata-rata penjualan
# dengan data yang terdapat dalam file sales.txt
def main():
    
    # Ikuti petunjuk pada komentar di bawah.
    # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
    # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah
    # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
    # dan variabel akumulator untuk menghitung total penjualan
    banyak = 0
    total = 0
    
    # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
    file = open('sales.txt','r')
    
    # [3] Tuliskan loop for untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
    # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
    # - inkrementasi variabel penghitung baris
    for baris in file:
        baris = float(baris)
        total += baris
        banyak += 1
    
    # [4] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
    # dan tampilkan hasilnya.        
    rata = total/banyak
    print(f'Rata-rata penjualan: {rata:,.2f}')

# Panggil fungsi main
main()