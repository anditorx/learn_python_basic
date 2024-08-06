class Bird:
    def fly(self):
        return "Bird is flying."

class Airplane:
    def fly(self):
        return "Airplane is flying."

# Fungsi yang menggunakan polimorfisme
def make_it_fly(entity):
    print(entity.fly())

# Membuat objek dari kelas yang berbeda
bird = Bird()
airplane = Airplane()

make_it_fly(bird)      # Output: Bird is flying.
make_it_fly(airplane)  # Output: Airplane is flying.
