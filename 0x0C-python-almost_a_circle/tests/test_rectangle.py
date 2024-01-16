#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangle_instantiation
    TestRectangle_order_of_initialization
    TestRectangle_area
    TestRectangle_update_args
    TestRectangle_update_kwargs
    TestRectangle_to_dictionary
"""
import unittest
import io
import os
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Test the instantiation and initialization of the Rectangle instances"""

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_instantiation(self):
        r = Rectangle(5, 3, 1, 2, 12)
        self.assertIsInstance(r, Base)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 12)

    def test_instantiation_with_default_values(self):
        r = Rectangle(5, 3)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_instantiation_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(1)
        with self.assertRaises(TypeError):
            r = Rectangle(5, 3, 1, 2, 12, 2, 4)

    def test_instantiation_multiple_rectangles(self):
        r1 = Rectangle(5, 3)
        r2 = Rectangle(4, 1)
        self.assertNotEqual(r1.id, r2.id)
        self.assertTrue(r1.id < r2.id)

    def test_instantiation_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 3).__width)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 3).__height)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 3).__x)
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 3).__y)

    def test_instantiation_getter(self):
        r = Rectangle(5, 3, 1, 2, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 12)

    def test_instantiation_setter(self):
        r = Rectangle(5, 3, 1, 2)
        r.width = 7
        self.assertEqual(r.width, 7)
        r.height = 4
        self.assertEqual(r.height, 4)
        r.x = 2
        self.assertEqual(r.x, 2)
        r.y = 3
        self.assertEqual(r.y, 3)


class TestRectangleAttributes(unittest.TestCase):
    """Unittests for validating attributes of the Rectangle class."""

    def test_width_validation(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("invalid", 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 5)

    def test_height_validation(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(5, "invalid")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(5, 0)

    def test_x_validation(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(5, 10, "invalid")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(5, 10, -1)

    def test_y_validation(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(5, 10, 2, "invalid")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(5, 10, 2, -1)


class TestRectangleArea(unittest.TestCase):
    """Unittests for the area method of the Rectangle class."""

    def test_area_with_valid_values(self):
        r = Rectangle(4, 6)
        self.assertEqual(r.area(), 24)

    def test_area_with_valid_values(self):
        r = Rectangle(8, 7)
        self.assertEqual(r.area(), 56)

    def test_area_with_zero_values(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, -6).area()

    def test_area_with_negative_values(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -6).area()

    def test_area_with_one_arg(self):
        r = Rectangle(5, 4)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Unittests for the display method of the Rectangle class."""

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
        r = Rectangle(4, 3, 0, 0)
        expected_output = "####\n####\n####\n"
        r.display()
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_with_x_and_y_offset(self):
        r = Rectangle(3, 2, 2, 1)
        expected_output = "\n  ###\n  ###\n"
        r.display()
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

    def test_display_with_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(2)


class TestRectangleStr(unittest.TestCase):
    """Unittests for the str method of the Rectangle class."""

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_str_representation(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(r), expected_output)

    def test_str_representation_default_id(self):
        r = Rectangle(3, 7, 1, 1)
        expected_output = "[Rectangle] (1) 1/1 - 3/7"
        self.assertEqual(str(r), expected_output)

    def test_str_representation_no_coordinates(self):
        r = Rectangle(4, 6)
        expected_output = "[Rectangle] (1) 0/0 - 4/6"
        self.assertEqual(str(r), expected_output)

    def test_str_method_changed_attributes(self):
        r = Rectangle(5, 3, 1, 0, 4)
        r.width = 7
        r.height = 2
        r.x = 4
        r.y = 1
        expected_output = "[Rectangle] (4) 4/1 - 7/2"
        self.assertEqual(str(r), expected_output)

    def test_str_with_one_arg(self):
        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.__str__(2)


class TestRectangleUpdate(unittest.TestCase):
    """Unittests for the update method of the Rectangle class."""

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_update_with_args(self):
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(6, 7, 8, 9, 10)
        self.assertEqual("[Rectangle] (6) 9/10 - 7/8", str(r))

    def test_update_args_one(self):
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(6)
        self.assertEqual("[Rectangle] (6) 1/2 - 3/4", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(12, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (12) 4/5 - 2/3", str(r))

    def test_update_with_None_id(self):
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(None, 5, 6)
        self.assertEqual("[Rectangle] (None) 1/2 - 5/6", str(r))

    def test_update_with_kwargs(self):
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(id=6, height=7, width=8, x=9, y=10)
        self.assertEqual("[Rectangle] (6) 9/10 - 8/7", str(r))

    def test_update_kwargs_one(self):
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(id=6)
        self.assertEqual("[Rectangle] (6) 1/2 - 3/4", str(r))

    def test_update_args_more_than_five(self):
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(id=12, width=2, height=3, length=7, x=4, y=5, z=6)
        self.assertEqual("[Rectangle] (12) 4/5 - 2/3", str(r))

    def test_update_with_None_id(self):
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(id=None, x=5, width=6)
        self.assertEqual("[Rectangle] (None) 5/2 - 6/4", str(r))


class TestRectangleToDictionary(unittest.TestCase):
    """Unittests for the to_dictionary method of the Rectangle class."""

    def test_to_dictionary(self):
        r = Rectangle(4, 5, 1, 2, 10)
        expected_dict = {"id": 10, "width": 4, "height": 5, "x": 1, "y": 2}
        self.assertEqual(r.to_dictionary(), expected_dict)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_with_default_args(self):
        r = Rectangle(5, 3)
        expected_dict = {"id": 1, "width": 5, "height": 3, "x": 0, "y": 0}
        self.assertEqual(r.to_dictionary(), expected_dict)
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_to_dictionary_no_object_changes(self):
        r1 = Rectangle(10, 2, 1, 9, 5)
        r2 = Rectangle(5, 9, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
