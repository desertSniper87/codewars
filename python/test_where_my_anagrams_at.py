import unittest
from where_my_anagrams_at import *

class AnagramTest(unittest.TestCase):
    def test_anagrams(self):
        # self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        # self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
        self.assertEqual(anagrams('big', ['gig', 'dib', 'bid', 'biig']), [])
        # self.assertEqual(anagrams('abba', ['gig', 'dib', 'bid', 'biig']), [])


# ['a', 'b', 'c', 'd', 'aabb', 'bbaa', 'abab', 'baba', 'baab', 'abcd', 'abbba', 'baaab', 'abbab', 'abbaa', 'babaa']
def main():
    unittest.main()

if __name__=="__main__":
    main()
