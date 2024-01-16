#!/usr/bin/python3
"""Defines unittests for models/square.py.

Unittest classes:
    TestSquare_instantiation
    TestSquare_order_of_initialization
    TestSquare_area
    TestSquare_stdout
    TestSquare_update_args
    TestSquare_update_kwargs
    TestSquare_to_dictionary
"""
import io
import sys
import unittest
from unittest.mock import patch
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestSquareInstantiation(unittest.TestCase):
    """Test the instantiation and initialization of the Square instances"""

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_instantiation(self):
        s = Square(5, 1, 2, 12)
        self.assertTrue(isinstance(s, (Base, Rectangle, Square)))
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 12)

    def test_instantiation_with_default_values(self):
        s = Square(5)
        self.assertTrue(isinstance(s, (Base, Rectangle, Square)))
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_instantiation_args(self):
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            r = Square(4, 3, 1, 2, 12, 2, 4)

    def test_instantiation_multiple_rectangles(self):
        s1 = Square(4)
        s2 = Square(5)
        self.assertNotEqual(s1.id, s2.id)
        self.assertTrue(s1.id < s2.id)

    def test_instantiation_private(self):
        with self.assertRaises(AttributeError):
            print(Square(5).__size)
        with self.assertRaises(AttributeError):
            print(Square(5).__height)
        with self.assertRaises(AttributeError):
            print(Square(5).__x)
        with self.assertRaises(AttributeError):
            print(Square(5).__y)

    def test_instantiation_getter(self):
        s = Square(5, 3, 1, 2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 1)
        self.assertEqual(s.id, 2)

    def test_instantiation_setter(self):
        s = Square(5, 3, 1)
        s.width = 7
        self.assertEqual(s.size, 7)
        s.x = 2
        self.assertEqual(s.x, 2)
        s.y = 3
        self.assertEqual(s.y, 3)


class TestSquareAttributes(unittest.TestCase):
    """Unittests for validating attributes of the Square class."""

    def test_size_validation(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("invalid")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)

    def test_x_validation(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(5, "invalid")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(5, -1)

    def test_y_validation(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(5, 2, "invalid")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(5, 2, -1)


class TestSquareArea(unittest.TestCase):
    """Unittests for the area method of the Square class."""

    def test_area_with_valid_values(self):
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_area_with_valid_values(self):
        s = Square(8)
        self.assertEqual(s.area(), 64)

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_with_non_integer_values(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid").area()

    def test_area_with_zero_values(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0).area()

    def test_area_with_negative_values(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-6).area()

    def test_area_with_one_arg(self):
        s = Square(5, 4)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquareDisplay(unittest.TestCase):
    """Unittests for the display method of the Square class."""

    def setUp(self):
        """
        Set up test environment by creating a mock stdout stream and starting a
        patcher.

        This method is called before each test case. It creates a mock stdout
        stream and starts a patcher to capture standard output (stdout) to be
        used during the tests.

        The mock_stdout stream is assigned to sys.stdout,
        and the patcher is started.

        Examples:
            Mocking stdout stream to capture output:
            self.mock_stdout = io.StringIO()
            self.patcher = patch("sys.stdout", new_callable=io.StringIO)
            self.mock_stdout = self.patcher.start()
        """
        self.mock_stdout = io.StringIO()
        self.patcher = patch("sys.stdout", new_callable=io.StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        """
        Clean up test environment by closing the mock stdout stream and
        stopping the patcher.

        This method is called after each test case. It closes the mock stdout
        stream and stops the patcher used for capturing standard output stdout
        during the tests.

        Examples:
            Closing the mock stdout stream:
            self.mock_stdout.close()

            Stopping the patcher:
            self.patcher.stop()
        """
        self.mock_stdout.close()
        self.patcher.stop()

    def test_display_with_valid_dimensions(self):
        s = Square(4, 0, 0)
        expected_output = "####\n####\n####\n####\n"
        s.display()
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_with_x_and_y_offset(self):
        s = Square(3, 2, 2)
        expected_output = "\n\n  ###\n  ###\n  ###\n"
        s.display()
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_with_one_arg(self):
        s = Square(5, 2, 4, 7)
        with self.assertRaises(TypeError):
            s.display(2)


class TestSquareStr(unittest.TestCase):
    """Unittests for the str method of the Square class."""

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_str_representation(self):
        s = Square(5, 2, 3)
        expected_output = "[Square] (1) 2/3 - 5"
        self.assertEqual(str(s), expected_output)

    def test_str_representation_default_id(self):
        s = Square(3, 1, 1)
        expected_output = "[Square] (1) 1/1 - 3"
        self.assertEqual(str(s), expected_output)

    def test_str_representation_no_coordinates(self):
        s = Square(4)
        expected_output = "[Square] (1) 0/0 - 4"
        self.assertEqual(str(s), expected_output)

    def test_str_method_changed_attributes(self):
        s = Square(5, 3, 1, 3)
        s.size = 5
        s.x = 3
        s.y = 1
        expected_output = "[Square] (3) 3/1 - 5"
        self.assertEqual(str(s), expected_output)

    def test_str_with_one_arg(self):
        s = Square(5, 2, 4, 7)
        with self.assertRaises(TypeError):
            s.__str__(2)


class TestSquareUpdate(unittest.TestCase):
    """Unittests for the update method of the Square class."""

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_update_with_args(self):
        s = Square(3, 1, 2, 5)
        s.update(6, 8, 9, 10)
        self.assertEqual("[Square] (6) 9/10 - 8", str(s))

    def test_update_args_one(self):
        s = Square(3, 1, 2, 5)
        s.update(6)
        self.assertEqual("[Square] (6) 1/2 - 3", str(s))

    def test_update_args_more_than_five(self):
        s = Square(3, 1, 2, 5)
        s.update(12, 3, 5, 6)
        self.assertEqual("[Square] (12) 5/6 - 3", str(s))

    def test_update_with_None_id(self):
        s = Square(3, 1, 2, 5)
        s.update(None, 5, 6)
        self.assertEqual("[Square] (None) 6/2 - 5", str(s))

    def test_update_with_kwargs(self):
        s = Square(3, 1, 2, 5)
        s.update(id=6, size=7, x=9, y=10)
        self.assertEqual("[Square] (6) 9/10 - 7", str(s))

    def test_update_kwargs_one(self):
        s = Square(3, 1, 2, 5)
        s.update(id=6)
        self.assertEqual("[Square] (6) 1/2 - 3", str(s))

    def test_update_args_more_than_five(self):
        s = Square(3, 1, 2, 5)
        s.update(id=12, size=2, length=7, x=4, y=5, z=6)
        self.assertEqual("[Square] (12) 4/5 - 2", str(s))

    def test_update_with_None_id(self):
        s = Square(3, 1, 2, 5)
        s.update(id=None, x=5, size=6)
        self.assertEqual("[Square] (None) 5/2 - 6", str(s))


class TestSquareToDictionary(unittest.TestCase):
    """Unittests for the to_dictionary method of the Square class."""

    def test_to_dictionary(self):
        s = Square(4, 1, 2, 10)
        expected_dict = {"id": 10, "size": 4, "x": 1, "y": 2}
        self.assertEqual(s.to_dictionary(), expected_dict)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_to_dictionary_with_default_args(self):
        s = Square(5)
        expected_dict = {"id": 1, "size": 5, "x": 0, "y": 0}
        self.assertEqual(s.to_dictionary(), expected_dict)
        self.assertIsInstance(s.to_dictionary(), dict)

    def test_to_dictionary_no_object_changes(self):
        s1 = Square(2, 1, 9, 2)
        s2 = Square(9, 1, 2, 3)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        s = Square(2, 4, 1, 4)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
