# Contoh penggunaan pernyataan kondisional untuk memeriksa apakah sebuah angka positif, negatif, atau nol

# Input dari pengguna
angka = float(input("Masukkan sebuah angka: "))

# Menggunakan kondisi untuk menentukan apakah angka positif, negatif, atau nol
if angka > 0:
    print("Angka tersebut adalah positif.")
elif angka < 0:
    print("Angka tersebut adalah negatif.")
else:
    print("Angka tersebut adalah nol.")
