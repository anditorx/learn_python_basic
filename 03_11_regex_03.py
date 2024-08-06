# Regex (regular expressions) di Python adalah alat yang sangat kuat untuk pencocokan pola di dalam teks. 
# Dengan regex, Anda dapat melakukan pencarian, penggantian, dan pemisahan teks berdasarkan pola tertentu. 
# Python memiliki modul re yang menyediakan fungsi untuk bekerja dengan regex.

import re

# Pencarian Semua Kemunculan
# Menggunakan fungsi re.findall() untuk menemukan semua kemunculan pola di dalam string.

pattern = r'\d+'  # Mencari semua angka
text = 'Ada 123 apel dan 456 jeruk.'
matches = re.findall(pattern, text)

print("Ditemukan:", matches)
