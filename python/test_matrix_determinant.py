import unittest


from matrix_determinant import *


m1 = [[1, 3], [2,5]]
m2 = [[2,5,3], [1,-2,-1], [1, 3, 4]]


class TestMatrix(unittest.TestCase):
    def setUp(self):
        pass

    def testMain(self):
        # self.assertEqual(determinant([[1]]), 1)
        # self.assertEqual(determinant(m1), -1)
        self.assertEqual(determinant(m2), -20)


def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


if __name__ == '__main__':
    main()

