with open('kota.txt', 'r') as infile:

    kota1 = infile.readline()
    kota2 = infile.readline()
    kota3 = infile.readline()

kota1 = kota1.rstrip('\n')
kota2 = kota2.rstrip('\n')
kota3 = kota3.rstrip('\n')

print('Baris 1:', kota1)
print('Baris 2:', kota2)
print('Baris 3:', kota3)