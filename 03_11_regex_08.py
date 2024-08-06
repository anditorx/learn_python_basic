# Regex (regular expressions) di Python adalah alat yang sangat kuat untuk pencocokan pola di dalam teks. 
# Dengan regex, Anda dapat melakukan pencarian, penggantian, dan pemisahan teks berdasarkan pola tertentu. 
# Python memiliki modul re yang menyediakan fungsi untuk bekerja dengan regex.

import re
# Grup Penangkapan
# Menggunakan tanda kurung () untuk menangkap bagian dari pola yang cocok.

pattern = r'(\d{3})-(\d{3})-(\d{4})'
text = 'Nomor telepon: 123-456-7890'
match = re.search(pattern, text)

if match:
    print("Kode area:", match.group(1))
    print("Bagian tengah:", match.group(2))
    print("Empat digit terakhir:", match.group(3))
