class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini.")

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def speak(self):
        return f"{self.name} says Chirp!"

    def fly(self):
        return f"{self.name} can fly." if self.can_fly else f"{self.name} cannot fly."

# Membuat objek dari kelas turunan
parrot = Bird("Polly", True)
penguin = Bird("Pingu", False)

print(parrot.speak())  # Output: Polly says Chirp!
print(parrot.fly())    # Output: Polly can fly.
print(penguin.speak())  # Output: Pingu says Chirp!
print(penguin.fly())    # Output: Pingu cannot fly.
