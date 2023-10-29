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
        ...

    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...

def main():
    my_jar = Jar()


if __name__ == "__main__":
      main()
