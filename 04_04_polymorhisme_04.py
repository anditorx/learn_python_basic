class Shape:
    def area(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini.")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Membuat objek dari kelas turunan
shapes = [Circle(5), Rectangle(4, 6)]

# Menggunakan polimorfisme untuk menghitung area dari setiap shape
for shape in shapes:
    print(shape.area())
# Output:
# 78.5
# 24
