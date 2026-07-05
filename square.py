#!/usr/bin/python3
"""Module with the class square"""
from base import Base
from rectangle import Rectangle


class Square(Rectangle):
    """class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a square"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return the attribute size"""
        return self.__width

    @size.setter
    def size(self, value):
        """sets the attribute size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """return a string representation of the square"""
        return str(f"[Square] ({self.id}) {self.x}/{self.y} - " +
                   f"{self.size}")

    def update(self, *args, **kwargs):
        """update the attributes using args or kwargs"""
        if args is not None and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        new_dic = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return new_dic
