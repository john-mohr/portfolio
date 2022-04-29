"""
Closest pair problem

This returns the closest pair of numbers.

Usage:

    python closest_pair.py [size of list of numbers]

John David Mohr and Jasper Ladkin

8/24/2021
"""

import random
import sys

'''
return the distance between two parameters
'''


def distance(a, b):
    return abs(a - b)


'''
populate the array with listSize unique random numbers between 1 ... 5000
'''


def populate(listSize):
    a = []
    count = 0

    while count < listSize:
        number = random.randint(1, 5000)
        if number in a:
            continue
        else:
            a.append(number)
            count += 1

    return a


'''
now determine the closest pair
using brute force algorithm
'''


def closest_pair(values):
    pt_a = -100
    pt_b = 100
    for i in range(len(values)):
        for x in range(len(values)):
            if(i != x):
                if distance(values[i], values[x]) < distance(pt_a, pt_b):
                    pt_a = values[i]
                    pt_b = values[x]

    closest = [pt_a, pt_b]
    return closest


'''
This behaves just like the Java main() method
'''
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage python Closest.py [number of points]')
        quit()
    else:
        numbers = populate(int(sys.argv[1]))

        closest = closest_pair(numbers)

        print('The closest numbers are', closest[0], 'and', closest[1])

