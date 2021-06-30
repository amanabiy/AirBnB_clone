#!/usr/bin/python3
"""
Unittest Module for FileStorage
"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    ''' Unittest for FileStorage class '''

    def test_Instantiation(self):
        ''' checks instance is of class BaseModel '''
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_Access(self):
        ''' test read-write access permissions '''
        rd = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(rd)
        wr = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(wr)
        ex = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertTrue(ex)

    def test_funcdocs(self):
        ''' testing functions docstring '''
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_save(self):
        ''' tests save method'''
        obj = FileStorage()
        new_obj = BaseModel()
        obj.new(new_obj)
        dict1 = obj.all()
        obj.save()
        obj.reload()
        dict2 = obj.all()
        for key in dict1:
            key1 = key
        for key in dict2:
            key2 = key
        self.assertEqual(dict1[key1].to_dict(), dict2[key2].to_dict())


if __name__ == '__main__':
    unittest.main()
