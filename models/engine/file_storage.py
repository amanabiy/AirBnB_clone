#!/usr/bin/python3
"""
Module file_storage
Contains a class FileStorage
that serializes instances to a JSON file and deserializes JSON file to instances
"""
import os.path
from os import path
import json
from models.base_model import BaseModel


class FileStorage:
    """
    that serializes instances to a JSON file and deserializes JSON file
    """
    """ initializing values """
    __file_path = "file.json"
    __objects = {}

    def all(self):
      """ returns the dictionary __objects """
      return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        if obj:
            """ adds the object and the key to __objects if the obj exists """
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        my_dic = {}

        for keys, obje in self.__objects.items():
            """ serialize each object using the key """
            my_dic[keys] = obje.to_dict()

        with open(self.__file_path, "w") as my_file:
            json.dump(my_dic, my_file)

    def reload(self):
        """ deserializes the JSON file to __objects """

        if path.exists(self.__file_path):

            with open(self.__file_path, 'r') as f:
                """ open the file and dessiralize it """
                new_obj = json.load(f)

            for key, value in new_obj.items():
                """ create each object and add it to the __objects """
                obj = BaseModel(**value)
                self.__objects[key] = obj
        else:
            pass
