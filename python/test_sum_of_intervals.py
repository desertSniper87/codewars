import unittest


from sum_of_intervals_2 import *


class IntervalTest(unittest.TestCase):
    def test(self):
        # self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        # self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        # self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
        # self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
        self.assertEqual(sum_of_intervals([(22, 33), (70, 249), (140, 406), (160, 467), (145, 402)]), 408)
        self.assertEqual(sum_of_intervals([(83, 227), (223, 456), (66, 418)]), 408)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
