def salam(nama="Teman"):
    print(f"Halo, {nama}!")
    
def info(nama, usia):
    print(f"Nama: {nama}, Usia: {usia}")



# call function
salam()         # Menggunakan nilai default
salam("Alice")  # Menggunakan nilai yang diberikan

info("Alice", 30)          # Positional arguments
info(nama="Bob", usia=25) 
