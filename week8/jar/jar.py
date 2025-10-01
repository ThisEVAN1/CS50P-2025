class Jar:
    def __init__(self, capacity=12, size=0):
        self._capacity = capacity
        self._size = size
        if capacity < 0:
            raise ValueError('Capacity has to be possitive')

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        # If the size + n is greater than the capacity then raise ValueError
        if self.size + n > self.capacity:
            raise ValueError('Not enough capacity')
        self._size += n

    def withdraw(self, n):
        # Check if there are enough cookies to be withdrawn
        if self.size - n < 0:
            raise ValueError('Not enough cookies to withdraw')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
