class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            raise ValueError("Age cannot be negative.")

# Membuat objek
person = Person("John", 30)

# Mengakses atribut menggunakan properti
print(person.name)  # Output: John
print(person.age)   # Output: 30

# Mengubah atribut menggunakan properti
person.age = 35
print(person.age)   # Output: 35

# Akan menghasilkan error jika umur negatif
# person.age = -5  # ValueError: Age cannot be negative.
