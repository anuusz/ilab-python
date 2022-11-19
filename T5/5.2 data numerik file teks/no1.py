def main():
    angka1 = float(input('Masukkan sebuah angka desimal: '))
    angka2 = float(input('Masukkan sebuah angka desimal lainnya: '))
    angka3 = float(input('Masukkan sebuah angka desimal lainnya: '))

    output_file = open('angka.txt', 'w')
    output_file.write(str(angka1) + '\n')
    output_file.write(str(angka2) + '\n')
    output_file.write(str(angka3) + '\n')

    print('Data telah berhasil disimpan dalam file angka.txt.')

main()