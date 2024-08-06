class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Membuat objek dari kelas turunan
generic_animal = Animal("Generic")
dog = Dog("Rex")

print(generic_animal.speak())  # Output: Generic makes a sound.
print(dog.speak())             # Output: Rex says Woof!
