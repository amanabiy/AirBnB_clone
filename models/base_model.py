#!/usr/bin/python3
"""
Module base_model
Contains a Class that defines all common attributes or
methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """ a base class for other classes """
    def __init__(self, *args, **kwargs):
        """ initializes the values """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ print in "[<class name>] (<self.id>) <self.__dict__>" format"""
        return ("[{}] (<{}>) <{}>".format(
            self.__class__.__name__,
            self.id,
            self.__class__.__dict__))

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keysvalues
        of __dict__ of the instance
        """
        my_dic = self.__dict__
        my_dic["__class__"] = self.__class__.__name__
        my_dic["updated_at"] = self.updated_at.isoformat()
        my_dic["created_at"] = self.created_at.isoformat()
        return my_dic
