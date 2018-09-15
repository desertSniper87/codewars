import unittest
from RouteCalculator import *

class TestRouteCalculator(unittest.TestCase):
    def test_route(self):
        tests = [
            ["1.1", 1.1],                   # returns the number if no commands given
            ["10+5", 15],                   # addition
            ["8-2", 6],                     # subtraction
            ["4*3", 12],                    # muliplication
            ["18$2", 9],                    # division
            ["5+8-8*2$4", 9],               # multiple commands
            ["3x+1", "400: Bad request"]    # handles incorrect input
        ]

        for test in tests:
            self.assertEqual(calculate(test[0]), test[1])

def main():
        unittest.main()

if __name__ == '__main__':
    main()
