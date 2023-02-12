jumlah = int(input('Masukan jumlah baris angka :'))
count = 0
a = 0
b = 1

while count < jumlah:
    print(a)
    jumlah_terakhir = a + b
    a = b
    b = jumlah_terakhir
    count += 1
