#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init of the class with id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """This method return width of triangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width values set"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """This method return height of triangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height values set"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Method for get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method set for get x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Method for get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method set for get y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return rectangle area"""
        return self.__width * self.__height

    def display(self):
        """Rectangle with character #"""
        for cont1 in range(self.__y):
            print()
        for cont2 in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self):
        """Update the class Rectangle"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height))
