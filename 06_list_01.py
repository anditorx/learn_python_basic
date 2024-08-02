# List adalah tipe data built-in yang digunakan untuk menyimpan koleksi elemen yang bisa diubah (mutable). 
# Elemen di dalam list dapat memiliki berbagai tipe data dan dapat diubah setelah list dibuat.
# Sintaksis: Didefinisikan dengan tanda kurung siku [] dan elemen-elemen dipisahkan oleh koma.

# Membuat list
buah_buahan = ["apel", "pisang", "jeruk"]

# Menambahkan elemen
buah_buahan.append("mangga")

# Mengubah elemen
buah_buahan[1] = "kiwi"

# Menghapus elemen
buah_buahan.remove("jeruk")

# Mengakses elemen
print(buah_buahan[0])  # Output: apel
print("----------")
# Iterasi melalui list
for buah in buah_buahan:
    print(buah)
