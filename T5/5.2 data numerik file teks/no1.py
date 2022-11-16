outfile = open('angka.txt', 'w')

des1 = input('Masukan sebuah angka desimal: ')
des2 = input('Masukan sebuah angka desimal lainnya: ')
des3 = input('Masukan sebuah angka desimal lainnya: ')

outfile.write(str(des1) + '\n')
outfile.write(str(des2) + '\n')
outfile.write(str(des3) + '\n')

outfile.close()

print("Data telah berhasil disimpan dalam file angka.txt")