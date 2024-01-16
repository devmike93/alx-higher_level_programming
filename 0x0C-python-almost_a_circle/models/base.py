#!/usr/bin/python3
"""This module defines the Base class."""
import json
import csv
import turtle


class Base:
    """The Base class manages unique IDs for instances of derived classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a unique ID or a provided 'id'."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.
        """
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Serialize a list of instances and save them as JSON data to a file.

        Args:
            cls: The class itself, used to determine the filename.
            list_objs (list): A list of instances to be serialized and saved.
        """
        if list_objs is None:
            list_objs = []

        file_name = f"{cls.__name__}.json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(Base.to_json_string(obj_dicts))

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Args:
            cls: The class itself.
        """
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                json_string = file.read()
                if json_string:
                    dict_list = Base.from_json_string(json_string)
                    instance_list = [cls.create(**item) for item in dict_list]
        except FileNotFoundError:
            return []

        return instance_list

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class with attributes set from a
        dictionary

        Args:
            cls: The class itself.
            **dictionary: A dictionary containing attribute values for the new
                          instance.

        Returns:
            A new instance of the class with attributes set according to the
            dictionary.
        """
        if dictionary:
            dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of objects and save them to a CSV file.

        Args:
            cls (type): The class type.
            list_objs (list): List of objects to serialize.
        """
        file_name = f"{cls.__name__}.csv"

        with open(file_name, 'w', newline='') as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    field_names = ['id', 'width', 'height', 'x', 'y']
                else:
                    field_names = ['id', 'size', 'x', 'y']
                csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize objects from a CSV file and return a list of instances.

        Returns:
            list: List of instances deserialized from the CSV file.
        """
        file_name = f"{cls.__name__}.csv"

        try:
            with open(file_name, 'r', newline='') as csv_file:
                if cls.__name__ == 'Rectangle':
                    field_names = ['id', 'width', 'height', 'x', 'y']
                else:
                    field_names = ['id', 'size', 'x', 'y']
                csv_reader = csv.DictReader(csv_file, fieldnames=field_names)
                list_objs = [dict((k, int(v)) for k, v in d.items())
                             for d in csv_reader]
        except FileNotFoundError:
            return []

        return [cls.create(**d) for d in list_objs]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draw a list of rectangles and squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to be drawn.
            list_squares (list): A list of Square objects to be drawn.
        """
        t = turtle.Turtle()
        t.screen.bgcolor("black")
        t.pensize(2)
        t.shape("turtle")

        t.color("#ffffff")
        for rect in list_rectangles:
            t.showturtle()
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.hideturtle()

        t.color("#b4e3d8")
        for square in list_squares:
            t.showturtle()
            t.up()
            t.goto(square.x, square.y)
            t.down()
            for i in range(4):
                t.forward(square.width)
                t.left(90)
            t.hideturtle()

        t.exitonclick()
