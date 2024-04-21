#!/usr/bin/python3
""" unittest """
import unittest


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

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