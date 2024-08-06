class Cat:
   
    spesies = "Kucing"
    
    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe
        
    def run(self, speed):
        print(f"Kucing {self.nama} berlari dengan {speed}...")
        
    def play(self):
        print(f"Kucing {self.nama} bermain dengan kopi lainnya...")
    
    def eat(self):
        pass
    
    
# Membuat object
kinako = Cat(nama="Kinako", tipe="Anggora")
minto = Cat(nama="Minto", tipe="Persia")

print(f"Kinako adalah seekor {kinako.__class__.spesies}")
print(f"{kinako.nama} merupakan kucing jenis {kinako.tipe}")
print(f"{minto.nama} merupakan kucing jenis {minto.tipe}")

# print(kinako.nama)
# print(minto.tipe)

kinako.run("cepat")
print(kinako.__doc__)