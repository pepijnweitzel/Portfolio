# Code created by Pepijn Weitzel

class Jar:
    def __init__(self, capacity=12):
        capacity = int(capacity)
        if capacity < 1:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    my_jar = Jar()
    print(my_jar)


if __name__ == "__main__":
      main()
