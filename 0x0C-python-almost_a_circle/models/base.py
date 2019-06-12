#!/usr/bin/python3
"""This class will be the base of the project."""
import json


class Base:
    """ Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Defines public attribute id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
