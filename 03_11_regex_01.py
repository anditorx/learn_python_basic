# Regex (regular expressions) di Python adalah alat yang sangat kuat untuk pencocokan pola di dalam teks. 
# Dengan regex, Anda dapat melakukan pencarian, penggantian, dan pemisahan teks berdasarkan pola tertentu. 
# Python memiliki modul re yang menyediakan fungsi untuk bekerja dengan regex.

import re

# Pencocokan Sederhana
# Menggunakan fungsi re.match() untuk memeriksa apakah suatu string cocok dengan pola tertentu.


pattern = r'hello'
text = 'hello world'
match = re.match(pattern, text)

if match:
    print("Cocok!")
else:
    print("Tidak cocok.")
