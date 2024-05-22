#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit tests for max_integer function"""

    def test_positive(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed(self):
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([1, -3, -4, 2]), 2)
        self.assertEqual(max_integer([4, -3, 2, -1]), 4)

    def test_one(self):
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([1.1, 3.3, 4.4, 2.2]), 4.4)
        self.assertEqual(max_integer([4.4, 3.3, 2.2, 1.1]), 4.4)

    def test_string(self):
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")
        self.assertEqual(max_integer(["hello", "world"]), "world")

    def test_same(self):
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
