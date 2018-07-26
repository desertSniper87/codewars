import unittest
from next_bigger_number_with_the_same_digits import *

class TestClass(unittest.TestCase):
    """Test"""
    def test_bigger(self):
        self.assertEqual(next_bigger(12),21)
        self.assertEqual(next_bigger(513),531)
        self.assertEqual(next_bigger(2017),2071)
        self.assertEqual(next_bigger(414),441)
        self.assertEqual(next_bigger(144),414)
        self.assertEqual(next_bigger(1234567890),1234567908)
        self.assertEqual(next_bigger(59884848459853),59884848483559)
        self.assertEqual(next_bigger(1195),1519)
        self.assertEqual(next_bigger(2988),8289)

def main():
    unittest.main()

if __name__=='__main__':
    main()


        

