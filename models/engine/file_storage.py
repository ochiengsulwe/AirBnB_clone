#!/usr/bin/python3
"""Defines a class FileStorage.
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """Serializes instance to JSON file and deserializes JSON file to instances

    Attributes:
        __file_path (str): Represents the path to the JSON file where
            instances will be serialized.
        __objects (dict): Stores all objects by <class name>.id for
            serialization and deserialization.

            Example: {'BaseModel.12121212': <BaseModel instance>}
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objects.

        Returns:
            dict: objects.
        """
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (any): object.
        """
        key = f"{obj.__class__.__name__ }.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path).
        """
        s_data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as myFile:
            json.dump(s_data, myFile)

    def reload(self):
        """Deserializes the JSON file to __objects.

        only if the JSON file(__file_path) exists ;
        otherwise, it does nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as myFile:
                d_data = json.load(myFile)
                self.__objects = {}
                for key, obj_dict in d_data.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj):
        """Deletes obj from __objects
        """
        try:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            del self.__objects[key]
            return True
        except Exception:
            return False
