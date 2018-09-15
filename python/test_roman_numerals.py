import unittest
from roman_numerals import *

class Test(unittest.TestCase):
    def test_roman_num(self):
        # self.assertEqual(RomanNumerals.to_roman(2000), 'MM')
        # self.assertEqual(RomanNumerals.to_roman(1), 'I')
        # self.assertEqual(RomanNumerals.to_roman(4), 'IV')
        # self.assertEqual(RomanNumerals.to_roman(5), 'V')
        # self.assertEqual(RomanNumerals.to_roman(7), 'VII')
        # self.assertEqual(RomanNumerals.to_roman(13), 'XIII')
        # self.assertEqual(RomanNumerals.to_roman(15), 'XV')
        # self.assertEqual(RomanNumerals.to_roman(20), 'XX')
        self.assertEqual(RomanNumerals.to_roman(1990), 'MCMXC')

def main():
    unittest.main()

if __name__=="__main__":
    main()

