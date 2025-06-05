class Rectangle:
    def __init__(self, length=10, width=5):
        self.length = length
        self.width = width
    def calculate_area(self):
        P = self.length * self.width
        print(f'Площадь = {P}')
    def draw(self):
        l = self.width - 1
        for i in range(self.length):
            print("*"* self.width)
class Square(Rectangle):
    def __init__(self, storona=3):
        super().__init__(storona, storona)
r1 = Rectangle()
r2 = Rectangle(5, 3)
r3 = Square()
r3.calculate_area()