import unittest
from Circle import Point
from Circle import Circle
from math import pi


class TestCirlceArea(unittest.TestCase):

    def setUp(self):
        self.test_point = Point(2, 2)
        self.test_circle = Circle(5, self.test_point)
        self.expected_point = Point(4, 4)

    def test_area(self):
        self.assertEqual(self.test_circle.area(), 78.53981633974483)
        self.assertEqual(self.test_circle.perimetr(), 31.41592653589793)
