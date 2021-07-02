#!/usr/bin/python3
import json
from os import path
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
"""
Module file_storage
Contains a class FileStorage
that serializes instances to a JSON file and
deserializes JSON file to instances
"""


class FileStorage():
    """
    that serializes instances to a JSON file and deserializes JSON file
    """
    ''' initializing values '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        if obj:
            ''' adds the object and the key to __objects if the obj exists '''
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[name] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        my_dict = {}

        for key, val in self.__objects.items():
            ''' serialize each object using the key '''
            my_dict[key] = val.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        ''' deserializes/loads the JSON file to __objects '''

        if not path.exists(self.__file_path):
            pass
        else:
            with open(self.__file_path, "r") as file_path:
                obj = json.load(file_path)
            for key, val in obj.items():
                self.__objects[key] = eval(val["__class__"])(**val)
