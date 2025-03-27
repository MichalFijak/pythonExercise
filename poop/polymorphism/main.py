
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self,height,base):
        self.height=height
        self.base=base

    def area(self):
        return (self.height*self.base)/2


class Pizza(Circle):
    def __init__(self, radius,topping):
        super().__init__(radius)
        self.topping=topping

shapes = [Circle(4),Square(5),Triangle(6,7),Pizza(15,"pepperoni")]

for shape in shapes:
    print(shape.area())