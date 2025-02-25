class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        total = self.size + n
        if total > self.capacity:
            raise ValueError("It won't fit!")
        else:
            self.size = total
        return self.size


    def withdraw(self, n):
        sub = self.size - n
        if sub < 0:
            raise ValueError("There are not that many cookies!")
        else:
            print("Nom nom nom.")
            self.size = sub
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity:
            raise ValueError("You must provide a number")
        elif capacity < 0:
            raise ValueError("Invalid number!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(8)
    print(jar)
    jar.withdraw(3)
    print(jar)

if __name__ == "__main__":
    main()

