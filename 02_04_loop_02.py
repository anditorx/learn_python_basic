# Menggunakan loop while untuk iterasi dari 1 sampai 20
angka = 1

while angka <= 20:
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan genap")
    else:
        print(f"{angka} adalah bilangan ganjil")
    angka += 1
