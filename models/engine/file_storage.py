#!/usr/bin/python3
"""Define class FileStorage"""
import json


class FileStorage(object):
    """Define class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Function to return var __objects

        Returns:
            dict: list of objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id

        :rtype: object
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)

        :rtype: object
        """
        with open(self.__file_path, "w") as my_file:
            my_file.write(json.dumps(FileStorage.__objects.items()))

    def reload(self):
        """deserializes the JSON file to __objects

        :rtype: object
        """
        if self.__file_path is not None:

            with open(self.__file_path) as f:
                new_dict = json.loads(f)
                for value in new_dict.value():
                    name = value['__class__']
                    del value['__class__']
                    self.new(eval(name)(**value))
