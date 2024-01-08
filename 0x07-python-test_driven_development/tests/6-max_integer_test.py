#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for the function max_integer()"""

    def test_max_integer_normal_list(self):
        """Test with a list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([10, 0, -10, 100, -100]), 100)

    def test_max_integer_normal_list(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.89, 3.54, -9.112, 17.2, -10.9]), 17.2)

    def test_max_integer_single_element(self):
        """Test with an empty list or containing a single element"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-42]), -42)

    def test_max_integer_char_list(self):
        """Test with a list of strings and characters"""
        self.assertEqual(max_integer("azerty"), 'z')
        self.assertEqual(max_integer('a'), 'a')
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(["one", "two", "three"]), "two")

    def test_max_integer_boll_list(self):
        """Test with a list of bools and integer"""
        self.assertEqual(max_integer([True, False]), True)

    def test_max_integer_errors(self):
        """Test for errors"""
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([None, 1, 5])
        with self.assertRaises(TypeError):
            max_integer(['a', 4, 2, 1])
        with self.assertRaises(TypeError):
            max_integer(["Hello", 4, 2, 1])


if __name__ == "__main__":
    unittest.main()
