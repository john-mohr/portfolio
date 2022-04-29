"""

Jasper Ladkin
John David Mohr

8/24/2021

"""
import unittest

import Closest


class Test(unittest.TestCase):
    def testClosest(self):

        expected = [-13, -14]
        self.assertEqual(expected, Closest.closest_pair([-13, 20, 5, 7, -14, 27]))

        expected = [-13, -13]
        self.assertEqual(expected, Closest.closest_pair([-13, 20, 5, 7, -13, 27]))

        expected = [7, 9]
        self.assertEqual(expected, Closest.closest_pair([-12,-7,-2,3,7,9]))

        expected = [-3, 1]
        self.assertEqual(expected, Closest.closest_pair([-30, -3, 1, 8, 13, 19]))





if __name__ == "__main__":
    unittest.main()
