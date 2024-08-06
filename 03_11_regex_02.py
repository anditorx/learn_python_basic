# Regex (regular expressions) di Python adalah alat yang sangat kuat untuk pencocokan pola di dalam teks. 
# Dengan regex, Anda dapat melakukan pencarian, penggantian, dan pemisahan teks berdasarkan pola tertentu. 
# Python memiliki modul re yang menyediakan fungsi untuk bekerja dengan regex.

import re

# Pencarian
# Menggunakan fungsi re.search() untuk mencari pola di dalam string.

pattern = r'world'
text = 'hello world'
match = re.search(pattern, text)

if match:
    print("Ditemukan:", match.group())
else:
    print("Tidak ditemukan.")

