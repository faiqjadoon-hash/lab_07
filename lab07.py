def count_occurrences(target, values):
    if values == []:
        return 0
    first = 1 if values[0] == target else 0
    return first + count_occurrences(target, values[1:])


def is_sorted(values):
    if len(values) <= 1:
        return True
    return values[0] <= values[1] and is_sorted(values[1:])


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"{self.width}x{self.height}"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


def main():
    print(count_occurrences(2, [1, 2, 2, 3, 2]))   # 3
    print(is_sorted([1, 2, 3]))                    # True
    print(Rectangle(3, 4).area())                  # 12
    print(Square(5))                               # 5x5


if __name__ == "__main__":
    main()