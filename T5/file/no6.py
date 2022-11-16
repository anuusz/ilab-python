tambah_kota = input('Masukkan nama kota: ')

output_file = open('kota.txt', 'a')

output_file.write(tambah_kota)

output_file.close()

print('Data telah ditambahkan ke file kota.txt.')