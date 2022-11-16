input_file = open('kota.txt', 'r')

isi_file = input_file.read()

input_file.close()

print(isi_file)



with open('kota.txt', 'r') as file:
    print('Jakarta')
    print('Bandung')
    print('Depok')

