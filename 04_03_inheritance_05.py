class Canine:
    def bark(self):
        return "Bark!"

class Feline:
    def meow(self):
        return "Meow!"

class DogCat(Canine, Feline):
    pass

# Membuat objek dari kelas turunan
creature = DogCat()

print(creature.bark())  # Output: Bark!
print(creature.meow())  # Output: Meow!
