class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        try:
            x = int(x)
        except ValueError:
            print("Must be a number")
            x = 0  # Default value if conversion fails
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        try:
            y = int(y)
        except ValueError:
            print("Must be a number")
            y = 0  # Default value if conversion fails
        self._y = y


def main():
    calculator = Calculator(0, 0)
    print(calculator.add(5, 3))


main()
