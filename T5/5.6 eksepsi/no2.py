try:
    y = int('x1010')
    print(y)
except IOError:
    print('Kode ini menyebabkan IOError.')
except ZeroDivisionError:
    print('Kode ini menyebabkan ZeroDivisionError.')
except:
    print('Sebuah error terjadi.')

# Sebuah Error terjadi.
# jangan lupa pake titik