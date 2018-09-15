import unittest

from triplets import *

class Triplet_Test(unittest.TestCase):
    def test_triplet(self):
        secret = "whatisup"
        triplets = [
          ['t','u','p'],
          ['w','h','i'],
          ['t','s','u'],
          ['a','t','s'],
          ['h','a','p'],
          ['t','i','s'],
          ['w','h','s']
        ]

        self.assertEqual(recoverSecret(triplets), secret)

def main():
        unittest.main()

if __name__ == "__main__":
    main()

