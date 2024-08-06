# Regex (regular expressions) di Python adalah alat yang sangat kuat untuk pencocokan pola di dalam teks. 
# Dengan regex, Anda dapat melakukan pencarian, penggantian, dan pemisahan teks berdasarkan pola tertentu. 
# Python memiliki modul re yang menyediakan fungsi untuk bekerja dengan regex.

import re

# Penggantian
# Menggunakan fungsi re.sub() untuk mengganti teks yang cocok dengan pola tertentu.

pattern = r'apel'
text = 'Saya suka apel.'
new_text = re.sub(pattern, 'jeruk', text)

print("Teks baru:", new_text)
