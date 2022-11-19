kota = ['Bandung', 'Jakarta', 'Medan', 'Surabaya']

with open('kota.txt', 'w') as output_file:
    output_file.writelines(kota)

# hasil outputnya:
# BandungJakartaMedanSurabaya