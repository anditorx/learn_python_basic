# Tuple adalah tipe data built-in yang digunakan untuk menyimpan koleksi elemen yang tidak dapat diubah (immutable). 
# Elemen dalam tuple bisa berupa berbagai tipe data.
# Sintaksis: Didefinisikan dengan tanda kurung biasa () dan elemen-elemen dipisahkan oleh koma.

# Membuat tuple
koordinat = (10, 20, 30)

# Mengakses elemen
print(koordinat[1])  # Output: 20
print("-------")
# Tuple dengan satu elemen
satu_elemen = (5,)

# Unpacking tuple
x, y, z = koordinat
print(f"x: {x}, y: {y}, z: {z}")  # Output: x: 10, y: 20, z: 30
print("-------")
# Tuple sebagai kunci dalam dictionary
lokasi = {(10, 20): "Kantor", (30, 40): "Rumah"}
print(lokasi[(10, 20)])  # Output: Kantor
