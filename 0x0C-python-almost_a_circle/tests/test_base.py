#!/usr/bin/python3
"""Defines unittests for models/base.py.

Unittest classes:
    TestBase_instantiation - line 21
    TestBase_to_json_string - line 108
    TestBase_save_to_file - line 154
    TestBase_from_json_string - line 232
    TestBase_create - line 286
    TestBase_load_from_file - line 338
    TestBase_save_to_file_csv - line 404
    TestBase_load_from_file_csv - line 482
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    """Test the instantiation and initialization of Base instances."""

    def test_negative_id(self):
        b = Base(-3)
        self.assertEqual(b.id, -3)

    def test_with_id(self):
        b = Base(4)
        self.assertIsInstance(b.id, int)
        self.assertEqual(b.id, 4)

    def test_None_id(self):
        bs1 = Base(None)
        bs2 = Base(None)
        self.assertNotEqual(bs1.id, bs2.id)
        self.assertTrue(bs2.id > bs1.id)

    def test_without_id(self):
        bs1 = Base()
        bs2 = Base()
        self.assertNotEqual(bs1.id, bs2.id)
        self.assertTrue(bs2.id > bs1.id)

    def test_id_public(self):
        bs = Base(7)
        bs.id = 19
        self.assertEqual(bs.id, 19)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_non_integer_id(self):
        self.assertEqual(Base(7.7).id, 7.7)
        self.assertEqual(Base("invalid").id, "invalid")
        self.assertEqual(Base({"one": 1, "two": 2}).id, {"one": 1, "two": 2})
        self.assertEqual(Base(["one", "two"]).id, ["one", "two"])


class TestBaseSerialization(unittest.TestCase):
    """
    Unittests for testing the 'to_json_string' method for seializing instances
    """

    def test_to_json_string_multipe_rectangle(self):
        rct1 = Rectangle(11, 8, 3, 8, 1)
        rct2 = Rectangle(9, 5, 1, 8, 2)
        result = (
                '[{"id": 1, "width": 10, "height": 8, "x": 3, "y": 8}, '
                '{"id": 3, "width": 9, "height": 5, "x": 1, "y": 8}]'
                )
        json_dicts = [rct1.to_dictionary(), rct2.to_dictionary()]
        self.assertEqual(Base.to_json_string(json_dicts), result)

    def test_to_json_string_rectangle(self):
        rct1 = Rectangle(10, 7, 2, 8, 5)
        result = '[{"id": 5, "width": 10, "height": 7, "x": 2, "y": 8}]'
        json_str = Base.to_json_string([rct1.to_dictionary()])
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, result)

    def test_to_json_string_square(self):
        sq1 = Square(7, 9, 1, 2)
        result = '[{"id": 2, "size": 7, "x": 9, "y": 1}]'
        json_str = Base.to_json_string([sq1.to_dictionary()])
        self.assertIsInstance(json_str, str)
        self.assertEqual(json_str, result)

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)

    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")


class TestBaseDeserialization(unittest.TestCase):
    """testing the 'from_json_string' method for deserializing instances."""

    def test_from_json_string_square(self):
        list_input = [
                {'id': 89, 'size': 10, 'x': 4, 'y': 2},
                {'id': 7, 'size': 1, 'x': 7, 'y': 1},
                ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)
        self.assertIsInstance(list_output, list)

    def test_from_json_string_rectangle(self):
        list_input = [
                {'id': 89, 'width': 10, 'height': 4},
                {'id': 7, 'width': 1, 'height': 7},
                ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)
        self.assertIsInstance(list_output, list)

    def test_from_json_string_empty_list(self):
        self.assertEqual(Base.from_json_string([]), [])
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

class TestJsonBaseFileOutput(unittest.TestCase):
    """Test the save_to_file method for writing instances to files."""

    def test_save_to_file_square(self):
        sq1 = Square(5, 3, 2)
        sq2 = Square(2, 4, 0)
        result = (
                '[{"id": 1, "size": 5, "x": 3, "y": 2}, '
                '{"id": 2, "size": 2, "x": 4, "y": 0}]'
                )
        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as file:
            json_data = file.read()
        self.assertIsInstance(json_data, str)
        self.assertEqual(json_data, result)

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_save_to_file_rectangle(self):
        rct1 = Rectangle(10, 7, 2, 8)
        rct2 = Rectangle(2, 4)
        result = (
                '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}, '
                '{"id": 2, "width": 2, "height": 4, "x": 0, "y": 0}]'
                )
        Rectangle.save_to_file([rct1, rct2])
        with open("Rectangle.json", "r") as file:
            json_data = file.read()
        self.assertIsInstance(json_data, str)
        self.assertEqual(json_data, result)

    def test_save_to_file_saves_object_data(self):
        s = Square(5, 7, 1)
        Base.save_to_file([s])
        with open("Base.json", "r") as file:
            self.assertTrue(len(file.read()) == 38)

    def test_save_to_file_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_overwrite(self):
        sq1 = Square(1)
        Square.save_to_file([sq1])
        sq2 = Square(2)
        Square.save_to_file([sq2])
        result = '[{"id": 2, "size": 2, "x": 0, "y": 0}]'
        with open("Square.json", "r") as file:
            json_data = file.read()
        self.assertIsInstance(json_data, str)
        self.assertEqual(json_data, result)

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], 1)

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def tearDown(self):
        """Clean up resources after each test case."""
        files_to_delete = ["Rectangle.json", "Square.json", "Base.json"]
        for filename in files_to_delete:
            if os.path.exists(filename):
                os.remove(filename)


class TestJsonBaseFileInput(unittest.TestCase):
    """Test the load_from_file method for reading instances from files."""

    def test_load_from_file_rectangle(self):
        sq1 = Square(1)
        sq2 = Square(2)
        Square.save_to_file([sq1, sq2])
        loaded_squares = Square.load_from_file()
        self.assertIsInstance(loaded_squares, list)
        self.assertTrue(len(loaded_squares) == 2)
        self.assertEqual(str(loaded_squares[0]), str(sq1))
        self.assertEqual(str(loaded_squares[1]), str(sq2))

    def test_load_from_file_rectangle(self):
        rct1 = Rectangle(4, 5, 1, 2)
        rct2 = Rectangle(3, 2, 2, 1)
        Rectangle.save_to_file([rct1, rct2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertIsInstance(loaded_rectangles, list)
        self.assertTrue(len(loaded_rectangles) == 2)
        self.assertEqual(str(loaded_rectangles[0]), str(rct1))
        self.assertEqual(str(loaded_rectangles[1]), str(rct2))

    def test_load_from_file_empty_file(self):
        with open("Rectangle.json", "w") as file:
            file.write("[]")
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 0)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_load_from_file_nonexistent_file(self):
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 0)
        self.assertEqual(rectangles, [])

    def tearDown(self):
        """Clean up resources after each test case."""
        files_to_delete = ["Rectangle.json", "Square.json", "Base.json"]
        for filename in files_to_delete:
            if os.path.exists(filename):
                os.remove(filename)


class TestBaseInstanceCreation(unittest.TestCase):
    """Test the create method for creating instances from dictionaries."""

    def test_create_from_dictionary_square(self):
        sq1 = Square(1, 2, 3)
        s1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**s1_dictionary)
        self.assertEqual(str(sq1), str(sq2))
        self.assertFalse(sq1 is sq2)
        self.assertFalse(sq1 == sq2)

    def test_create_from_empty_dictionary(self):
        empty_dict = {}
        rct1 = Rectangle.create(**empty_dict)
        self.assertEqual(rct1, None)

    def test_create_from_dictionary_rectangle(self):
        rct1 = Rectangle(3, 5, 1, 2)
        rct1_dictionary = rct1.to_dictionary()
        rct2 = Rectangle.create(**rct1_dictionary)
        self.assertEqual(str(rct1), str(rct2))
        self.assertFalse(rct1 is rct2)
        self.assertFalse(rct1 == rct2)


class TestCsvBaseFileOutput(unittest.TestCase):
    """Test the save_to_file_csv method for writing instances to files."""

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_save_to_file_csv_square(self):
        sq1 = Square(5, 3, 2)
        sq2 = Square(2, 4, 0)
        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "1,5,3,2\n2,2,4,0\n")

    def test_save_to_file_csv_rectangle(self):
        rct1 = Rectangle(10, 7, 2, 8)
        rct2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([rct1, rct2])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "1,10,7,2,8\n2,2,4,0,0\n")

    def test_save_to_file_csv_saves_object_data(self):
        s = Square(5, 7, 1)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as file:
            self.assertEqual(file.read(), "1,5,7,1\n")

    def test_save_to_file_csv_empty_list(self):
        Base.save_to_file_csv([])
        with open("Base.csv", "r") as file:
            self.assertEqual(file.read(), "[]")
        Base.save_to_file_csv(None)
        with open("Base.csv", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_csv_overwrite(self):
        sq1 = Square(1)
        Square.save_to_file_csv([sq1])
        sq2 = Square(2)
        Square.save_to_file_csv([sq2])
        with open("Square.csv", "r") as file:
            self.assertEqual(file.read(), "2,2,0,0\n")

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv([], 1)

    def tearDown(self):
        """Clean up resources after each test case."""
        files_to_delete = ["Rectangle.csv", "Square.csv", "Base.csv"]
        for filename in files_to_delete:
            if os.path.exists(filename):
                os.remove(filename)

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv()


class TestCsvBaseFileInput(unittest.TestCase):
    """Test the load_from_file_csv method for reading instances from files."""

    def setUp(self):
        """Reset the base class id counter"""
        Base._Base__nb_objects = 0

    def test_load_from_file_csv_rectangle(self):
        sq1 = Square(1)
        sq2 = Square(2)
        Square.save_to_file_csv([sq1, sq2])
        loaded_squares = Square.load_from_file_csv()
        self.assertEqual(str(loaded_squares[0]), str(sq1))
        self.assertEqual(str(loaded_squares[1]), str(sq2))

    def test_load_from_file_csv_rectangle(self):
        rct1 = Rectangle(4, 5, 1, 2)
        rct2 = Rectangle(3, 2, 2, 1)
        Rectangle.save_to_file_csv([rct1, rct2])
        loaded_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(str(loaded_rectangles[0]), str(rct1))
        self.assertEqual(str(loaded_rectangles[1]), str(rct2))

    def test_load_from_file_csv_nonexistent_file(self):
        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(rectangles), 0)
        self.assertEqual(rectangles, [])

    def test_load_from_file_csv_empty_file(self):
        """
        with open("Rectangle.csv", "w") as file:
            file.write("[]")
        rectangles = Rectangle.load_from_file_csv()
        self.assertEqual(len(rectangles), 0)
        """
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

    def tearDown(self):
        """Clean up resources after each test case."""
        files_to_delete = ["Rectangle.csv", "Square.csv", "Base.csv"]
        for filename in files_to_delete:
            if os.path.exists(filename):
                os.remove(filename)


if __name__ == "__main__":
    unittest.main()
