def main():
    
    angka = [234, 694, 123, 789, 923, 674, 534]

    with open ('list_angka.txt', 'w') as file:
        for i in angka:
            i =  str(i)
            file.write(i + '\n')

main()