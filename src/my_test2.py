class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if(__name__ == '__main__'):
    a = Triangle(10, 10)
    print(a.area())
    print(a.area())