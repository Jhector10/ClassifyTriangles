import math
import unittest

""" This function returns a string with the type of triangle from three values

        return:
            If all three sides are equal, return 'Equilateral'
            If exactly one pair of sides are equal, return 'Isoceles'
            If no pair of  sides are equal, return 'Scalene'
            If not a valid triangle, then return 'NotATriangle'
            If the sum of any two sides equals the equate of the third side, then return 'Right'

        """
def classify_triangle(a, b, c):
    right_triangle1 = pow(a, 2) + pow(b, 2)
    right_triangle2 = pow(b, 2) + pow(c, 2)
    right_triangle3 = pow(c, 2) + pow(a, 2)
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not Valid"
    elif a == b and b == c:
        return "Equilateral"
    elif (right_triangle1 == pow(c, 2)) or (right_triangle2 == pow(a, 2)) or (right_triangle3 == pow(b, 2)) and (a != b and a != c and b != c):
        return "Scalene Right"
    elif (right_triangle1 == pow(c, 2)) or (right_triangle2 == pow(a, 2)) or (right_triangle3 == pow(b, 2)) and (a == b or a == c or b == c):
        return "Isosceles Right"
    elif a == b or a == c or b == c:
        return "Isosceles"
    elif a != b and a != c and b != c:
        return "Scalene"

""" Now this is the area that will include the test cases """

class TestTriangle(unittest.TestCase):
    """ Create this class so that the test cases can be called """

    def test_equal(self):
        self.assertEqual(classify_triangle(6, 6, 6), "Equilateral")
        self.assertEqual(classify_triangle(100, 100, 100), "Equilateral")

    def test_notvalid(self):
        self.assertEqual(classify_triangle(0, 0, 0), "Not Valid")
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
    unittest.main(exit=False)
      
