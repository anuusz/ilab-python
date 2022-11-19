angka = [1, 2, 3, 4, 5]

with open('daftar_angka.txt', 'w') as output_file:
    output_file.writelines(angka)

# program menghasilkan eror