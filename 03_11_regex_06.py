# Regex (regular expressions) di Python adalah alat yang sangat kuat untuk pencocokan pola di dalam teks. 
# Dengan regex, Anda dapat melakukan pencarian, penggantian, dan pemisahan teks berdasarkan pola tertentu. 
# Python memiliki modul re yang menyediakan fungsi untuk bekerja dengan regex.

import re
# Kumpulan Karakter
# Menggunakan tanda kurung siku [] untuk mencocokkan satu karakter dari sekumpulan karakter.

pattern = r'[aeiou]'  # Mencocokkan vokal
text = 'hello world'
matches = re.findall(pattern, text)

print("Vokal yang ditemukan:", matches)
