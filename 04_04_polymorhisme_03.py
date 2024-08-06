class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Cow:
    def speak(self):
        return "Moo!"

# Membuat daftar objek dari kelas yang berbeda
animals = [Dog(), Cat(), Cow()]

# Menggunakan polimorfisme untuk memanggil metode pada setiap objek
for animal in animals:
    print(animal.speak())
# Output:
# Woof!
# Meow!
# Moo!
