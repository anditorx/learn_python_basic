class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I'm quacking like a duck!"

# Fungsi yang menggunakan duck typing
def make_it_quack(entity):
    print(entity.quack())

# Membuat objek dari kelas yang berbeda
duck = Duck()
person = Person()

make_it_quack(duck)   # Output: Quack!
make_it_quack(person) # Output: I'm quacking like a duck!
