#!/usr/bin/python3
"""Unittest for Square Class
"""
import unittest
from models.square import Square

class TestSquareClass(unittest.TestCase):
    
    def test__fail_init(self):
        """Test if square class can be initialized"""
        with self.assertRaises(TypeError):
            Square()

