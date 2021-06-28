#!/usr/bin/python3
import unittest
from models.user import User
"""
Unittest Module for User class
"""


class TestUser(unittest.TestCase):
    ''' Unittest for User class '''

    def test_object_Instantiation(self):
        ''' instantiates class '''
        self.user = User()
        
    def testattr(self):
        ''' test Class: User attributes '''
        self.user = User()
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertFalse(hasattr(self.user, "random_attr"))
        self.assertFalse(hasattr(self.user, "name"))
        self.assertTrue(hasattr(self.user, "id"))
        self.user.name = "Alice"
        self.user.age = "44"
        self.assertTrue(hasattr(self.user, "name"))
        self.assertTrue(hasattr(self.user, "age"))
        delattr(self.user, "name")
        self.assertFalse(hasattr(self.user, "name"))
        delattr(self.user, "age")
        self.assertFalse(hasattr(self.user, "age"))
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
        self.assertEqual(self.user.__class__.__name__, "User")
        self.user.first_name = "Alice"
        self.user.last_name = "Bob"
        self.user.email = "Alice@gmail.com"
        self.user.password = "Al23ba4f$58"
        self.assertEqual(self.user.email, "Alice@gmail.com")
        self.assertEqual(self.user.password, "Al23ba4f$58")
        self.assertEqual(self.user.first_name, "Alice")
        self.assertEqual(self.user.last_name, "Bob")

    def testsave(self):
        ''' testing method: save '''
        self.user = User()
        self.user.save()
        self.assertTrue(hasattr(self.user, "updated_at"))

    def teststr(self):
        ''' testing __str__ return format of User '''
        self.user = User()
        s = "[{}] ({}) {}".format(self.user.__class__.__name__,
                                    str(self.user.id), self.user.__dict__)
        self.assertEqual(print(s), print(self.user))

if __name__ == '__main__':
    unittest.main()
