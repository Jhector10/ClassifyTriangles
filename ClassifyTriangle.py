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
    if (a + b <= c) or (a + c <= b) or (b + c <= a) or a <= 0 or b <= 0 or c <= 0:
        return "Not Valid"
    elif not(isinstance(a,int or float) and isinstance(b,int or float) and isinstance(c,int or float)):
        return "Not Valid"
    elif a == b and b == c:
        return "Equilateral"
    elif ((pow(a, 2) + pow(b, 2)) == pow(c, 2)) or ((pow(b, 2) + pow(c, 2)) == pow(a, 2)) or ((pow(c, 2) + pow(a, 2)) == pow(b, 2)) and (a != b and a != c and b != c):
        return "Scalene Right"
    elif ((pow(a, 2) + pow(b, 2)) == pow(c, 2)) or ((pow(b, 2) + pow(c, 2)) == pow(a, 2)) or ((pow(c, 2) + pow(a, 2)) == pow(b, 2)) and (a == b or a == c or b == c):
        return "Isosceles Right"
    elif a == b or a == c or b == c:
        return "Isosceles"
    elif a != b and a != c and b != c:
        return "Scalene"