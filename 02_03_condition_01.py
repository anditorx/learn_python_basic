# Contoh penggunaan pernyataan kondisional if, elif, dan else

# Input dari pengguna
nilai = int(input("Masukkan nilai ujian Anda: "))

# Menggunakan kondisi untuk menentukan nilai huruf
if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B'
elif nilai >= 70:
    grade = 'C'
elif nilai >= 60:
    grade = 'D'
else:
    grade = 'F'

# Menampilkan hasil
print(f"Nilai huruf Anda adalah {grade}")