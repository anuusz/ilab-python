import random

def main():

    outfile = open('daftar_angka.txt', 'w')
    for i in range(1, 101):
        outfile.write(str(i) + '\n')
    outfile.close()
          
main()