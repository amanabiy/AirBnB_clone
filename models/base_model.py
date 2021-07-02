#!/usr/bin/python3
"""
Module base_model
Contains a Class that defines all common attributes or
methods for other classes
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    ''' a base class for other classes '''

    def __init__(self, *args, **kwargs):
        '''
        initializes the values
        '''
        if kwargs != {}:
            dtf = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if ("created_at" == k or "updated_at" == k):
                    setattr(self, k, datetime.strptime(v, dtf))
                elif not k == "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        print in "[<class name>] (<self.id>) <self.__dict__>" format
        '''
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__class__.__dict__))

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keysvalues
        of __dict__ of the instance
        '''
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
