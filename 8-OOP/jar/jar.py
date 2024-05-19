class Jar:

    def __init__(self, capacity=12):
        self.capacity = int(capacity)
        self.size = 0

    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n: int):
        self.size += n

    def withdraw(self, n: int):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        if capacity < 0:
            raise ValueError("Must be Positive")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: int):
        if size < 0:
            raise ValueError("Too few cookies to take")
        if size > self.capacity:
            raise ValueError("Exceeds jar capacity")
        self._size = size


def main():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(7)
    print(jar)


if __name__ == "__main__":
    main()
