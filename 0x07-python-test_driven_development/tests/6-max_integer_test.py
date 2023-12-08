#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer([..])
    """
    def test_max_integer(self):
        """Test max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_none_result(self):
        """test_none_result[]"""
        self.assertEqual(max_integer([]), None)
    def test_single_result(self):
        """test_single_result[]"""
        self.assertEqual(max_integer([9]), 9)
    def test_duplicate(self):
        self.assertEqual(max_integer([9,9,7,5]), 9)
    def test_negative(self):
        self.assertEqual(max_integer([-7,-9,-1]), -1)
    def test_float(self):
        self.assertEqual(max_integer([9.0,9.8,7,5]), 9.8)
