import unittest


from alphabetic_anagram import *



class TestAlphaAnagram(unittest.TestCase):
    def setUp(self):
        pass

    def testMain(self):
        testValues = {'A' : 1, 'ABAB' : 2, 'AAAB' : 1, 'BAAA' : 4, 'QUESTION' : 24572, 'BOOKKEEPER' : 10743}
        for word in testValues:
          print(word)
          self.assertEqual(listPosition(word), testValues[word])


def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


if __name__ == '__main__':
    main()

