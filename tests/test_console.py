#!/usr/bin/python3
from console import HBNBCommand
from unittest.mock import create_autospec
import unittest
import sys
"""
Unittest Module for console.py
"""


class TestConsole(unittest.TestCase):
    ''' Unittest for console.py module '''

    def SetUp(self):
        ''' setting the mock_stdin and mock_stdout '''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def test_Console(self, server=None):
        ''' instantiates Console for HBNBCommand '''
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_Quit(self):
        ''' tests quit method '''
        
        cmd = HBNBCommand()
        self.assertRaises(SystemExit, quit)

    def test_docs(self):
        ''' tests docstrings '''
        self.assertTrue(len(HBNBCommand.__doc__) > 0, "** There is No docstring Found ** ")       
