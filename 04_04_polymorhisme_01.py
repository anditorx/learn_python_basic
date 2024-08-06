class Animal:
    def speak(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini.")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Fungsi yang menggunakan polimorfisme
def make_animal_speak(animal):
    print(animal.speak())

# Membuat objek dari kelas turunan
dog = Dog()
cat = Cat()

make_animal_speak(dog)  # Output: Woof!
make_animal_speak(cat)  # Output: Meow!
