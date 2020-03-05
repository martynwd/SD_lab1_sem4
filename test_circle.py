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
        
    
    def test_perimetr(self):
        self.assertEqual(self.test_circle.perimetr(), 31.41592653589793)


    def test_plusvector(self):
        self.test_circle = self.test_circle.plusvector(self.test_point)
        self.assertEqual(self.test_circle.x, 4)
        self.assertEqual(self.test_circle.y, 4)

    def test_initial_value(self):
       self.assertEqual(self.test_circle.radius,5)
       self.assertEqual(self.test_circle.center.x,self.test_point.x)
       self.assertEqual(self.test_circle.center.y, self.test_point.y)
        

