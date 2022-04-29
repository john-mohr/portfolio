"""
@author: greg, jingsai
"""
import unittest

import Fibonacci


class Test(unittest.TestCase):
    def testFib(self):
        # sequence of size 0
        sequence = []
        self.assertEqual(sequence, Fibonacci.fibonacci(0))

        # sequence of size 1
        sequence = [0]
        self.assertEqual(sequence, Fibonacci.fibonacci(1))

        # sequence of size 2
        sequence = [0, 1]
        self.assertEqual(sequence, Fibonacci.fibonacci(2))

        # sequence of size > 2
        sequence = [0, 1, 1, 2, 3, 5]
        self.assertEqual(sequence, Fibonacci.fibonacci(6))


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
