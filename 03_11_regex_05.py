# Regex (regular expressions) di Python adalah alat yang sangat kuat untuk pencocokan pola di dalam teks. 
# Dengan regex, Anda dapat melakukan pencarian, penggantian, dan pemisahan teks berdasarkan pola tertentu. 
# Python memiliki modul re yang menyediakan fungsi untuk bekerja dengan regex.

import re
# Pemisahan
# Menggunakan fungsi re.split() untuk memisahkan string berdasarkan pola tertentu.

pattern = r'\s+'  # Memisahkan berdasarkan spasi
text = 'Ini adalah contoh teks.'
split_text = re.split(pattern, text)

print("Hasil pemisahan:", split_text)
