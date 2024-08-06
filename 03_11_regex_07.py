# Regex (regular expressions) di Python adalah alat yang sangat kuat untuk pencocokan pola di dalam teks. 
# Dengan regex, Anda dapat melakukan pencarian, penggantian, dan pemisahan teks berdasarkan pola tertentu. 
# Python memiliki modul re yang menyediakan fungsi untuk bekerja dengan regex.

import re
# Pengulangan
# Menggunakan {} untuk mencocokkan jumlah pengulangan tertentu.

pattern = r'\d{3}'  # Mencocokkan tiga digit angka berturut-turut
text = 'Nomor telepon: 123-456-7890'
matches = re.findall(pattern, text)

print("Tiga digit angka:", matches)
