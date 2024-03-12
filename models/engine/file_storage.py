#!/usr/bin/env python3
#  serializes instances to a JSON file and deserializes JSON file to instances:

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity


class FileStorage():
    """ this class defines methods to serialize and deserialize ogbects"""

    __file_path = "file.json"
    __objects = {}
    __active_classes = [
                        "BaseModel", "User", "Place", "State",
                        "City", "Amenity", "Review"
                       ]

    @property
    def objects(self):
        """Getter for the __objects attribute"""
        return FileStorage.__objects

    @property
    def file_path(self):
        """ Getters for the __file_path attribute"""
        return FileStorage.__file_path

    @property
    def active_classes(self):
        """Getter for the __active_classes attribute"""
        return FileStorage.__active_classes

    def all(self):
        """  returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        stores in __objects the
        object as value and <obj class name>.id as key
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as file1:
            serialized_objects = {}
            for key, obj in FileStorage.__objects.items():
                serialized_objects[key] = obj.to_dict()
            json.dump(serialized_objects, file1)

    def reload(self):
        """ deserializes the JSON file to __objects"""

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_dicts = json.load(f)
                for key, value in obj_dicts.items():
                    new_obj = eval(value["__class__"])(**value)
                    self.new(new_obj)
        except FileNotFoundError:
            pass
