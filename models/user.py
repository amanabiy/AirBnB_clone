#!/usr/bin/python3
from models.base_model import BaseModel
"""
Module class: User
"""


class User(BaseModel):
    """definition for class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
