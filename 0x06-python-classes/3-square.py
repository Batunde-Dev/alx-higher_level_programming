#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Defines a Square instance.
    Args:
            size (int): size of the square
    """

    def __init__(self, size=0):
        """Initializes the attribute 'size'.
        Args:
            __size (int): size of the square - private attribute
        Raises:
            TypeError: If size is not integer
            ValueError: If size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Class Square method.
        Returns:
            Area of square
        """

        area = self.__size * self.__size
        return area
