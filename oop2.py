import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 22/7 * self.radius **2
    def perimeter(self):
        return 22/7 * self.radius * 2
    def print_details(self):
        print("Radius",self.radius )
        print("Perimeter",self.perimeter())
        print("Area",self.area())

C1 = Circle(5)
C2= Circle(10)

C1.print_details()
print(C1.area())
print(C2.perimeter())



