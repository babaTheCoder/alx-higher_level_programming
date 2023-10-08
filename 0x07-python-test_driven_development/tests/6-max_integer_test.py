#!usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 1, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-3, -4, -5, -2]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -4, -5]), 2)
        self.assertEqual(max_integer([-1, -2, 3, 4]), 4)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 3, 4, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)

if __name__ == "__main__":
    unittest.main()
