"""
Updated March 14, 2021
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Joshua Hector
"""
import math
import unittest

from ClassifyTriangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangle(unittest.TestCase):
    """ Create this class so that the test cases can be called """

    def test_equal(self):
        self.assertEqual(classify_triangle(6, 6, 6), "Equilateral")
        self.assertEqual(classify_triangle(100, 100, 100), "Equilateral")

    def test_notvalid(self):
        self.assertEqual(classify_triangle(0, 0, 0), "Not Valid")
        self.assertEqual(classify_triangle(-3, -5, 6), "Not Valid")
        self.assertEqual(classify_triangle("1", "3", "5"), "Not Valid")
        self.assertEqual(classify_triangle(True, True, False), "Not Valid")
        self.assertNotEqual(classify_triangle(1, 10, 12), "Valid", "Should be an invalid triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(9, 9, 12), "Isosceles")
        self.assertNotEqual(classify_triangle(3, 4, 4), "Equilateral", "Should be Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(5, 8, 11), "Scalene")
        self.assertEqual(classify_triangle(4, 8, 9), "Scalene")

    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")
        self.assertNotEqual(classify_triangle(5, 12, 13), "Isosceles Right", "Should be Scalene Right")


if __name__ == '__main__':
    print(classify_triangle(6,6,6))
    print(classify_triangle(3,4,5))
    print(classify_triangle(9,9,12))
    print(classify_triangle(4,6,7))
    print(classify_triangle(3.2, 5.4, 8))
    unittest.main(exit=False)