try:
    x = float('abc123')
    print('Konversi berhasil.')
except IOError:
    print('Kode ini menyebabkan IOError.')
except ValueError:    
    print('Kode ini menyebabkan ValueError.')

# Kode ini menyebabkan ValueError.
# jangan lupa pake titik