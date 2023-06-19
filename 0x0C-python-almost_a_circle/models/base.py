#!/usr/bin/python3
"""the 'Base' class"""

import json


class Base:
    """definition  of Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """dict to json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json to file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dict_list)
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """listof dict"""
        a_list = []
        if json_string is not None and json_string != "":
            a_list = json.loads(json_string)
        return a_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            ret = cls(1, 1)
        if cls.__name__ == "Square":
            ret = cls(1)
        ret.update(**dictionary)
        return ret

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{:s}.json".format(cls.__name__)

        try:
            with open(filename, mode="r", encoding="utf-8") as a_file:
                content_string = a_file.read()
            a_list = cls.from_json_string(content_string)
            list_instances = []
            for i in range(len(a_list)):
                list_instances.append(cls.create(**a_list[i]))
        except Exception:
            list_instances = []

        return list_instances
