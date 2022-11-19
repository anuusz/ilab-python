def main():
    # List untuk menyimpan isi file
    list_angka = []
    
    # [1] Tuliskan statement yang meminta pengguna memasukkan nama file dengan prompt: Masukkan nama file: "
    a = str(input('Masukkan nama file: '))

    # [2] Tuliskan exception handler dengan statement try/except
    # Pada body klausa try: buka file, baca isinya, dan simpan isinya ke list_angka
    # Pada body klausa except untuk FileNoFoundError tampilkan pesan "File tidak ditemukan."
    # Pada body klausa except untuk ValueError tampilkan pesan "Terdapat data non numerik dalam file."
    # Pada body klausa else: Cari rata-rata, nilai tertinggi, nilai terenda dan tampilkan hasilnya
    try:
        with open(a,'r') as file:
            list_angka = file.readlines()
            i = 0
            while i < len(list_angka):
                list_angka[i] = list_angka[i].rstrip('\n')
                i+=1
            banyak = 0
            total = 0
            a = 0
            b = 0
            for j in list_angka:
                banyak += 1
                total += float(j)
    except FileNotFoundError:
        print('File tidak ditemukan.')
    except ValueError:
        print('Terdapat data non numerik dalam file.')
    else:
        rata = total/banyak
        nilai_tertinggi = max(list_angka)
        nilai_terendah = min(list_angka)
        print(f'Rata-rata nilai: {rata:,.2f}')
        print('Nilai tertinggi:',nilai_tertinggi)
        print('Nilai terendah:',nilai_terendah)
                
# Panggil fungsi main
main()