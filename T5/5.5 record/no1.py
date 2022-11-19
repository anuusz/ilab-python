# Program ini menambahkan record nilai mahasiswa
# ke file nilai_mahasiswa.txt
def main():
    # [1] Minta pengguna berapa banyak record yang ingin dimasukkan
    a = int(input('Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? '))

    # [2] Buka file dengan statement with, minta input masing-masing record ke pengguna, dan tulis ke file
    # nilai_mahasiswa.txt
    with open('nilai_mahasiswa.txt','a') as file:
        for i in range(1,a+1):
            print('Masukkan record nilai mahasiswa ke',str(i))
            nama = str(input('Nama: '))
            nilai = float(input('Nilai: '))
            print('')
            nilai = str(nilai)
            file.write(nama+'\n')
            file.write(nilai+'\n')

# Panggil fungsi main
main()