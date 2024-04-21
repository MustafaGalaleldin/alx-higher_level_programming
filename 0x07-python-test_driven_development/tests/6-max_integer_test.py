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
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4, 0, 3, 1]), 4)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()