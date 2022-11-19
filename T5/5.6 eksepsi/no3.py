# Program ini meminta pengguna memasukkan dua angka untuk operasi pembagian
# Program menampilkan pesan jika terjadi eksepsi
def main():
    # [1] Tuliskan statement try/except
    # Pada body klausa try:
    #     - Minta dua angka ke pengguna
    #     - Lakukan pembagian
    # Pada body klausa except untuk ValueError
    #     - Tampilkan pesan: "Nilai yang diinput salah."
    # Pada body klausa except untuk ZeroDivisionError
    #     - Tampilkan pesan: "Tidak dapat membagi dengan nol."
    try:
        a = int(input('Masukkan sebuah angka yang akan dibagi: '))
        b = int(input('Masukkan sebuah angka pembagi: '))
        c = a/b
        c = float(c)
        print(a,'dibagi dengan',b,'sama dengan',c)
    except ValueError:
        print('Nilai yang diinput salah.')
    except ZeroDivisionError:
        print('Tidak dapat membagi dengan nol.')

# Panggil fungsi main
main()