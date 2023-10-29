# Code created by Pepijn Weitzel

class Jar:
    def __init__(self, capacity=12):
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

    @capacity.setter
    def capacity(self, capacity):
        capacity = int(capacity)
        if capacity < 1:
            raise ValueError
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size



def main():
    my_jar = Jar()
    


if __name__ == "__main__":
      main()
