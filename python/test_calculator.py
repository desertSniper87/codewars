# TODO: Replace examples and use TDD development by writing your own tests
# These are some of the methods available:
#   test.expect(boolean, [optional] message)
#   test.assert_equals(actual, expected, [optional] message)
#   test.assert_not_equals(actual, expected, [optional] message)

# You can use Test.describe and Test.it to write BDD style test groupings

import unittest
from calculator_jolaf import *

calc = Calculator()

class TestClass(unittest.TestCase):
    def test_calculator(self):
        self.assertEqual(calc.evaluate("2 / 2 + 3 * 4 - 6"), 7.0)
        self.assertEqual(calc.evaluate("2 - 3 - 4"), -5.0)
        self.assertEqual(calc.evaluate("2 + 3 * 4 / 3 - 6 / 3 * 3 + 8"), 8.0)

def main():
    unittest.main()

if __name__=="__main__":
    main()
