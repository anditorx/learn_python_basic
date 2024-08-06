'''
Enkapsulasi adalah salah satu prinsip utama dalam pemrograman berorientasi objek (OOP) yang digunakan untuk membatasi akses ke data dan metode dari objek. 
Enkapsulasi melindungi data dari modifikasi yang tidak sah dan memungkinkan untuk mengontrol bagaimana data dan metode diakses atau diubah. 
Di Python, enkapsulasi biasanya dicapai dengan menggunakan atribut privat dan properti.

'''
class Person:
    def __init__(self, name, age):
        self.__name = name  # Atribut privat
        self.__age = age    # Atribut privat

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

# Membuat objek
person = Person("John", 30)

# Mengakses atribut menggunakan metode getter
print(person.get_name())  # Output: John
print(person.get_age())   # Output: 30

# Mengubah atribut menggunakan metode setter
person.set_age(35)
print(person.get_age())   # Output: 35

# Tidak dapat mengakses atribut privat langsung
# print(person.__name)  # Ini akan menghasilkan error
