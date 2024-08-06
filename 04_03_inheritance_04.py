class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Memanggil konstruktor dari kelas dasar
        self.breed = breed

    def speak(self):
        return super().speak() + f" Specifically, a {self.breed} dog."

# Membuat objek dari kelas turunan
dog = Dog("Rex", "Golden Retriever")

print(dog.speak())  # Output: Rex makes a sound. Specifically, a Golden Retriever dog.
