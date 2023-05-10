class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    # 인스턴스 생성
    rect = Rectangle(5, 10)

    # 너비와 높이 출력
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")

    # 면적 출력
    print(f"Area: {rect.area()}")
