#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a Square instance."""

    def __init__(self, size=0):
        """The Square __init__ method initializes the attribute 'size'."""

        self.size = size

    @property
    def size(self):
        """Square getter method."""

        return self.__size

    @size.setter
    def size(self, value):
        """Square setter method."""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Square area method."""

        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character '#'"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
