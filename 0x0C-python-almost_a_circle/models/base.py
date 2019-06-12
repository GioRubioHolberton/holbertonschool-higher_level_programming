#!/usr/bin/python3
import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return("[]")
        return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        new_list = []
        if list_objs:
            for li_obj in list_objs:
                new_list.append(li_obj.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as file:
            file.write(cls.to_json_string(new_list))
