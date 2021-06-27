#!/usr/bin/python3
"""Unittest Module for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittest for Base class"""

    def test_nb_onject_Instantiation(self):
        """instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def test_nb_objects_private(self):
        """test nb_objects is private"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
