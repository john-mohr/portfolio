"""
    QuickHull.py
    Implementation of QuickHull algorithm

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


class QuickHull:

    def __init__(self):
        self.convexHullSet = []

    '''
    Given three Point objects, p, q, and r, 
    returns the determinant 
    '''
    def get_determinant(self, p, q, r):
        # Your code goes here:
        return ((q.x - p.x)*(r.y - p.y) - (q.y - p.y)*(r.x-p.x))
        #return ((p.x * q.y)+(r.x * p.y)+(q.x * r.y))-(r.x * q.y)-(q.x * p.x)-(p.x * r.y)

    '''
    Given two Point objects, p and q, 
    and a list of points, 
    returns the farthest point from the line between p1 and p2 
    '''
    def get_farthest_point(self, p1, p2, points):
        if len(points) == 0:
            return
        largest = points[0]
        for i in points:
            if self.get_determinant(p1,p2,i) > self.get_determinant(p1,p2,largest):
                largest = i
        return largest

    '''
    Given a sorted list of Point objects, sorted_points,
    computes the convex hull,
    where the convex hull is a list of Point objects starting at the
    extreme left point and going clockwise in order
    '''
    def convex_hull(self, sorted_points):
        convex_hull_set = []

        # start with the extreme left point
        p1 = sorted_points[0]

        # and the extreme right point
        pn = sorted_points[-1]

        #top half of the convex hull
        self.convexHullSet.append(p1)
        points = []

        for i in sorted_points:
            if self.get_determinant(p1, pn, i) > 0:
                points.append(i)

        self.quick_hull(p1, pn, points)

        #bottom half of the convex hull
        self.convexHullSet.append(pn)
        points = []

        for i in sorted_points:
            if self.get_determinant(pn, p1, i) > 0:
                points.append(i)

        self.quick_hull(pn, p1, points)
        self.convexHullSet.append(p1)
        # Your code goes here:

        return self.convexHullSet

    '''
    Recursive divide-and-conquer algorithm to find the convex hull 
    '''
    def quick_hull(self, p1, pn, points):
        # Your code goes here:
        leftPoints = []

        if len(points) == 0:
            if pn not in self.convexHullSet:
                self.convexHullSet.append(pn)
            return
        for i in points:
            if self.get_determinant(p1, pn, i) > 0:
                leftPoints.append(i)

        pMax = self.get_farthest_point(p1,pn, points)
        self.quick_hull(p1,pMax,leftPoints)
        self.quick_hull(pMax,pn,leftPoints)

'''
Extra Credit: find the closest pair of points using 
a divide and conquer algorithm 
'''
def closest_pair(points):
    if len(points) <= 2:
        return points
    #elif len(points) == 3:
    else:
        pt_a = points[0]
        pt_b = points[1]
        min_distance = pt_a.dist(pt_b)
        i = 2
        for pt in points:
            if pt is pt_a or pt is pt_b:
                current = pt.dist(points[i])
                if current < min_distance:
                    pt_a = pt
                    pt_b = points[i]
                    min_distance = current
        return (pt_a, pt_b)
#    else:


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
    hull = QuickHull()
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

    # optional extra credit
    #p1, p2 = closest_pair(sorted_points)
    #plt.plot([p1.x, p2.x], [p1.y, p2.y], 'm*')

    plt.show()


if __name__ == "__main__":
    main()
