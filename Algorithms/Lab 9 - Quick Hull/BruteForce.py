"""
    BruteForce.py
    Implementation of Brute Force algorithm to determine a Convex Hull

    [John David Mohr, Jasper Ladkin]
"""
import sys
import math
import matplotlib.pyplot as plt


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get the distance to another Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # string representation of a Point
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # equality tests of two Points - needed for sorting points
    def __eq__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__(self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y < other.y)
        return (self.x < other.x)

    def __le__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__(self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)

class ConvexHull:

    def __init__(self):
        self.convexHullSet = []

    '''
    Given two Point objects, p and q, 
    returns the standard form for line equation as a tuple (a, b, c)
    ax + by = c
    '''
    def get_line_equation(self, p, q):
        # Your code goes here:
        a, b = q.y - p.y, p.x - q.x
        c = (p.x * q.y) - (p.y * q.y)
        return [a, b, c]
        pass

    '''
    Given a line equation (ax + by = c) and a point pt,
    returns whether the point is inside the line 
    '''
    def is_inside(self, a, b, c, pt):
        return (a*pt.x + b*pt.y) > c

    '''
    Given a sorted list of Point objects, sorted_points,
    computes the convex hull,
    where the convex hull is a list of Point objects starting at the
    extreme left point and going clockwise in order
    '''
    def convex_hull(self, sorted_points):
        # start with the extreme left point
        p1 = sorted_points[0]
        self.convex_hull_set = [p1]

        # Your code goes here:
        #use while loop
        while true:
            for j in sorted_points:
                if j == i:

                    break
                    line = self.get_line_equation(i, j)
                    if self.line_search(line,sorted_points):
                        convex_hull.append(j)

        return self.convex_hull_set


    def line_search(self, line, sorted_points):
        for p in sorted_points:
            if not self.is_inside(line,p):
                return False

        return True





def main():
    # create an empty list of Point objects
    points_list = []

    # read number of points
    file = open('hull.in', 'r')
    line = file.readline().strip()
    num_points = int(line)
    x_values = []
    y_values = []
    # print(num_points, "points")

    # read data from standard input
    for i in range(num_points):
        line = file.readline().strip()
        line = line.split()
        x = int(line[0])
        y = int(line[1])
        points_list.append(Point(x, y))
        x_values.append(x)
        y_values.append(y)
        # print(x, y)
    file.close()

    # sort the list according to x-coordinates
    sorted_points = sorted(points_list)

    # get the convex hull
    hull = ConvexHull()
    convex_hull = hull.convex_hull(sorted_points)

    # print the convex hull
    # and extract x and y values for visualizing convex hull
    hull_x = []
    hull_y = []
    print("Convex Hull:")
    for p in convex_hull:
        print(str(p))
        hull_x.append(p.x)
        hull_y.append(p.y)

    # graph points and convex hull
    plt.plot(x_values, y_values, 'bo')
    plt.plot(hull_x, hull_y, 'r')
    plt.show()


if __name__ == "__main__":
    main()
