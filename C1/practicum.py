class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_params(self):
        return self.x, self.y, self.width, self.height

    def __str__(self):
        return f'Rectangle: {self.x, self.y, self.width, self.height}'

    def get_area(self):
        return self.width * self.height


rect_1 = Rectangle(5, 1, 10, 20)
print(rect_1)
print(f'Площадь прямоугольника rect_1: {rect_1.get_area()}')
