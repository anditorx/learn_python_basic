# Dictionary adalah tipe data built-in yang menyimpan pasangan kunci-nilai. 
# Dictionary bersifat mutable dan tidak terurut. Kunci harus bersifat hashable (immutable) seperti string, angka, atau tuple.
# Sintaksis: Didefinisikan dengan tanda kurung kurawal {} dan pasangan kunci-nilai dipisahkan oleh koma.

# Membuat dictionary
data_siswa = {
    "nama": "Alice",
    "usia": 22,
    "nilai": [85, 90, 88]
}

# Mengakses nilai berdasarkan kunci
print(data_siswa["nama"])  # Output: Alice

# Menambahkan atau mengubah nilai
data_siswa["alamat"] = "Jakarta"
data_siswa["usia"] = 23

# Menghapus pasangan kunci-nilai
del data_siswa["nilai"]

# Iterasi melalui dictionary
for kunci, nilai in data_siswa.items():
    print(f"{kunci}: {nilai}")
