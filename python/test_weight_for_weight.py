import unittest

from weight_for_weight import *


class WeightTest(unittest.TestCase):
    def test_weight(self):
        self.assertEqual(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        self.assertEqual(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")


def main():
    unittest.main()


if __name__ == '__main__':
    main()

