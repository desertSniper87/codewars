import unittest
from calculator_jolaf import *


class TestClass(unittest.TestCase):
    def test_choppa(self):
        grid1_blueprint = """
        S0110
        01000
        01010
        00010
        0001E
        """
        grid1, grid1_start, grid1_target = make_grid(grid1_blueprint, 5, 5)
        grid1_optimum_path = [
            grid1[0][0],
            grid1[0][1],
            grid1[0][2],
            grid1[0][3],
            grid1[1][3],
            grid1[2][3],
            grid1[2][2],
            grid1[2][1],
            grid1[3][1],
            grid1[4][1],
            grid1[4][2],
            grid1[4][3],
            grid1[4][4]
        ]
        print(grid1_blueprint)
        path = find_shortest_path(grid1, grid1_start, grid1_target)
        self.assertEquals(path, grid1_optimum_path)


def main():
    unittest.main()


if __name__=="__main__":
    main()
