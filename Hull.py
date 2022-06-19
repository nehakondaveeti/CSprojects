#  File: Hull.py

#  Description: Print the vertices of the convex hull clockwise. 

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 02/18

#  Date Last Modified: 02/18

import sys

import math

class Point (object):
    # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points:
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
        else:
            return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    x1 = p.x
    x2 = q.x
    x3 = r.x
    y1 = p.y
    y2 = q.y
    y3 = r.y
    det = (x1*(y2-y3) + x2 * (y3-y1) + x3 *(y1-y2))
    return det

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    #Sort points by x
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])

    for i in range(2,len(sorted_points)):
        upper_hull.append(sorted_points[i])
        while(len(upper_hull)>=3):
            if(det(upper_hull[len(upper_hull)-3],upper_hull[len(upper_hull)-1],upper_hull[len(upper_hull)-2])<0):
                upper_hull.pop(len(upper_hull)-2)
            else:
                break
    
    lower_hull = []
    lower_hull.append(sorted_points[len(sorted_points)-1])
    lower_hull.append(sorted_points[len(sorted_points)-2])

    for i in range(len(sorted_points)-3,-1,-1):
        lower_hull.append(sorted_points[i])
        while(len(lower_hull)>=3):
            if(det(lower_hull[len(lower_hull)-3],lower_hull[len(lower_hull)-1],lower_hull[len(lower_hull)-2])<0):
                lower_hull.pop(len(lower_hull)-2)
            else:
                break
    
    lower_hull.pop(0)
    lower_hull.pop(len(lower_hull)-1)

    #for p in lower_hull:
    #    print (str(p))

    convex_hull = upper_hull + lower_hull
    return convex_hull

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    det = 0
    for i in range(len(convex_poly)-1):
        det = det + (convex_poly[i].x*convex_poly[i+1].y) - (convex_poly[i].y*convex_poly[i+1].x)
        
    det = det + (convex_poly[len(convex_poly)-1].x*convex_poly[0].y) - (convex_poly[len(convex_poly)-1].y*convex_poly[0].x)
    area = abs(det) / 2
    return area

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
    return "all test cases passed"

def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int (line)

  # read data from standard input
    for i in range (num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int (line[0])
        y = int (line[1])
        points_list.append (Point (x, y))

    # sort the list according to x-coordinates
    sorted_points = sorted (points_list, key=lambda k: [k.x,k.y])
    ch = convex_hull(sorted_points)
    
    
     # print your results to standard output
     # print the convex hull
    sys.stdout.write('Convex Hull')
    sys.stdout.write('\n')
    for p in ch:
        sys.stdout.write(str(p))
        sys.stdout.write('\n')
    sys.stdout.write('\n')
    # get the area of the convex hull
    # print the area of the convex hull
    sys.stdout.write('Area of Convex Hull = '+ str(area_poly(ch)))
    sys.stdout.write('\n')
    

if __name__ == "__main__":
    main()