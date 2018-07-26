import unittest
from maximum_subarray_sum import *

class TestClass(unittest.TestCase):
    def test_subarray(self):
        self.assertEqual(maxSequence([]), 0)
        self.assertEqual(maxSequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]), 0)
        self.assertEqual(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

def main():
    unittest.main()

if __name__=="__main__":
    main()
