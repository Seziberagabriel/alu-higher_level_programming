#!/usr/bin/python3
""" Define a square class"""


class Square:
    """ rep... of a square class"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print('#' * self.size)
