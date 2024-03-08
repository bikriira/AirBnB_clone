#!/usr/bin/env python3
#  serializes instances to a JSON file and deserializes JSON file to instances:

import json
from models.base_model import BaseModel


class FileStorage():
    """ this class defines methods to serialize and deserialize ogbects"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""

        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""

        with open(self.__file_path, "w", encoding="utf-8") as file1:
            json.dump(FileStorage.__objects, file1)

    def reload(self):
        """ deserializes the JSON file to __objects"""

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dicts = json.load(f)
                for key, value in obj_dicts.items():
                    new_obj = BaseModel(**value)
                    self.new(new_obj)
        except FileNotFoundError:
            pass
