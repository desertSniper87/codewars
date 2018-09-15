from sum_by_factors import *
import unittest

class TestSumFactors(unittest.TestCase):
    def test_sum_by_factors(self):
        a = [12, 15]
        self.assertEqual(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])
        a = [15, 21, 24, 30, 45]
        self.assertEqual(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])
        a = [15, 21, 24, 30, -45]
        self.assertEqual(sum_for_list(a), [[2, 54], [3, 45], [5, 0], [7, 21]])
        a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
        print(sum_for_list(a))
        self.assertEqual(sum_for_list(a), [[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]])
 

def main():
    unittest.main()

if __name__ == "__main__":
    main()
