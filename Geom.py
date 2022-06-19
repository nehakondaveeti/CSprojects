

import math


# object oriented programming

class Point (object):
    # constructor
    def __init__(self, x = 0, y = 0):
        # this is a special function python knows
        # attributes are the x and y coordinate
        # intialize
        self.x = x
        self.y = y
        # self is a

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # test for equality of two Point objects
    def __eq__(self, other):
        tol = 1.0e-6
        return str(self.x - other.x) < tol and str(self.y - other.y) < tol
    # strign represenation of a Point object
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

        # test for equality of two Point objects
    def main():
        # create Point objects
        a = Point()
        b = Point (3,4)
        c = Point (3,4)

        # print the Point objects
        print(a)
        print(b)

        # test for equality of Point objects
        if (b ==c):
            print("Point objects are equal")
        else:
            print("Point objects are not equal")
        


