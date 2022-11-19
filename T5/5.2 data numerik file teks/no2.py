def main():
    
    infile = open('angka_float.txt', 'r')
    
    num1 = float(infile.readline())
    num2 = float(infile.readline())
    
    infile.close()

    jumlah = num1 * num2

    print('Baris 1 file angka_float.txt berisi:', num1)
    print('Baris 2 file angka_float.txt berisi:', num2)
    print('Hasil kali baris 1 dan baris 2 =', round(jumlah, 2))

main()