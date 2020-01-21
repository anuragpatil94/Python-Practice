"""
A dynamic array is an array with a big improvement: Automatic Resizing.

Space       O(n)    O(n)
Lookup      O(1)    O(1)
Append      O(1)    O(n)
insert      O(n)    O(n)
delete      O(n)    O(n)
"""


class DynamicArray:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.size = 0

    def __getitem__(self, key):
        return self.array[key]

    def __resize(self):
        self.array = self.array + [None] * self.capacity
        self.capacity *= 2

    def push(self, value):
        if self.size == self.capacity:
            self.__resize()
        self.array[self.size] = value
        self.size += 1

    def pop(self):
        x = self.array[-1]
        self.array[-1] = None
        self.size -= 1
        return x

    def currentCapacity(self):
        return self.capacity

    def __len__(self):
        return self.size
