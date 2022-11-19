# Program ini membaca file daftar_nilai.txt yang berisi data nilai ujian
# dari 30 mahasiswa dan mencari nilai rata-rata, nilai tertinggi, dan nilai terenda
def main():
    
    # Buat variabel untuk menyimpan hasil perhitungan dan inisialisasi dengan 0.0 (float)
    rata_rata = 0.0
    nilai_tertinggi = 0.0
    nilai_terendah = 0.0
    
    # [1] Tuliskan statement untuk membuka file daftar_nilai.txt untuk dibaca 
    # dan simpan isinya ke sebuah list
    with open('daftar_nilai.txt','r') as file:
        list = file.readlines()

    # [2] Tuliskan struktur loop untuk menghapus karakter baris baru pada setiap elemen
    # dari list
    i = 0
    while i < len(list):
        list[i] = list[i].rstrip('\n')
        i+=1
    
    # [3] Cari nilai rata-rata, nilai tertinggi, dan terendah. Gunakan loop.
    banyak = 0
    total = 0
    a = 0
    b = 0
    for j in list:
        j = float(j)
        banyak += 1
        total += j
    rata = total/banyak
    nilai_tertinggi = max(list)
    nilai_terendah = min(list)
    
    # [4] Tampilkan rata-rata, nilai tertinggi, dan nilai terendah.
    print(f'Rata-rata nilai ujian:  {rata:,.2f}')
    print('Nilai ujian tertinggi: ',nilai_tertinggi)
    print('Nilai ujian terendah: ',nilai_terendah)

# Panggil fungsi main()
main()