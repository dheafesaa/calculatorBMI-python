print('=====================================')
print('Menghitung rasio tinggi / berat badan')
print('=====================================')
print('Rumus indeks proporsi: berat_badan/tinggi_badan*tinggi_badan')
print('')

nama = input('Masukkan nama anda : ')
tinggi = eval(input('Tinggi badan (cm)  : '))
berat = eval(input('Berat badan (kg)   : '))

tinggi = tinggi/100
indeks = berat/(tinggi*tinggi)
print('Kisaran indeks     :', indeks)

if (indeks > 30):
    status = 'obesitas'
elif (indeks >= 25 and indeks < 38):
    status = 'kelebihan'
elif (indeks >= 18.5 and indeks < 25):
    status = 'normal'
else:
    status = 'kurang'

print('')
print('-----------------------------------------------')
print('Halo,', nama, 'anda masuk dalam kategori', status)
print('-----------------------------------------------')
