import math
"""
This imports Python’s math module, giving access to mathematical constants and functions.

We use math.pi to get the value of π (3.14159…).Formula for area of a circle:
Area=π×r2        Circumference=2×π×r    Circumference of the circle
"""
class circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
       return math.pi *self.radius**2
    def Circumference_area(self):
        return 2* math.pi*self.radius
obj=circle(10)
print('Area of the circle',obj.calculate_area())
print('Circumference of the circle',obj.Circumference_area())