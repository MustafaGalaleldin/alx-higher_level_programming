#!/usr/bin/python3
""" unittest """
import unittest
max_integer = __import__('6-max_integer').max_integer


class max_test(unittest.TestCase):
    """
    testing class
    """
    def test_1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_2(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    def test_3(self):
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
    def test_4(self):
        self.assertEqual(max_integer([]), None)
    def test_5(self):
        self.assertEqual(max_integer(), None)
    def test_6(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def test_7(self):
        self.assertEqual(max_integer([1]), 1)
    def test_8(self):
        self.assertEqual(max_integer([1, 2, -1]), 2)

if __name__ == '__main__':
    unittest.main()