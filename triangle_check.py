"""
Updated March 14, 2021
The primary goal of this file is to demonstrate a simple python
program to classify triangles

@author: Joshua Hector
"""
def classify_triangle(side_a, side_b, side_c):
    """ This function returns a string with the type of triangle from three values

        return:
            If all three sides are equal, return 'Equilateral'
            If exactly one pair of sides are equal, return 'Isoceles'
            If no pair of  sides are equal, return 'Scalene'
            If not a valid triangle, then return 'NotATriangle'
            If the sum of any two sides equals the equate of the third side, then return 'Right'

        """
    triangle = ''
    if ((side_a + side_b <= side_c)
        or (side_a + side_c <= side_b)
        or (side_b + side_c <= side_a)):
        triangle = "Not Valid"
    elif side_a <= 0 or side_b <= 0 or side_c <= 0:
        triangle = "Not Valid"
    elif (not(isinstance(side_a,int or float)
    and isinstance(side_b,int or float)
    and isinstance(side_c,int or float))):
        triangle = "Not Valid"
    elif side_a == side_b and side_b == side_c:
        triangle = "Equilateral"
    elif (((pow(side_a, 2) + pow(side_b, 2)) == pow(side_c, 2))
    or ((pow(side_b, 2) + pow(side_c, 2)) == pow(side_a, 2))
    or ((pow(side_c, 2) + pow(side_a, 2)) == pow(side_b, 2))):
        triangle = "Right"
    elif side_a != side_b and side_a != side_c and side_b != side_c:
        triangle = "Scalene"
    else:
        triangle = "Isosceles"

    return triangle
