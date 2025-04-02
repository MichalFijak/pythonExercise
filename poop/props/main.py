class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width} cm"
    
    @property
    def height(self):
        return f"{self._height} cm"
    
    def area(self):
        return self.width * self.height

    @width.setter
    def width(self, value):
        if value <= 0:
            raise print("Width must be positive")
        self._width = value

    @height.setter
    def height(self, value):
        if value <= 0:
            raise print("Height must be positive")
        self._height = value
    
    @width.deleter
    def width(self):
        print("Deleting width")
        del self._width

    @height.deleter
    def height(self):
        print("Deleting height")
        del self._height

# Example usage
rectangle = Rectangle(10, 5)
rectangle.width = 20
print(rectangle.area)  # Output: 50
print(rectangle.width)  # Output: 10
print(rectangle.height)  # Output: 5

del rectangle.width
del rectangle.height