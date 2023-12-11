#!/usr/bin/python3
"""Unittest for Base Class
"""
import unittest
from models.base import Base

class TestBaseClass(unittest.TestCase):

    def test__fail_init(self):
        """Test if Base class can be initialized"""
        with self.assertRaises(TypeError):
            Base()

