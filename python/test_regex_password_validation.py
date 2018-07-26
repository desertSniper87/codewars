from re import search
import unittest
from regex_password_validation import *

class Test(unittest.TestCase):
    def test_name(self):
        self.assertEqual(bool(search(regex, 'fjd3IR9')), True)
        self.assertEqual(bool(search(regex, 'ghdfj32')), False)
        self.assertEqual(bool(search(regex, 'DSJKHD23')), False)
        self.assertEqual(bool(search(regex, 'dsF43')), False)
        self.assertEqual(bool(search(regex, '4fdg5Fj3')), True)
        self.assertEqual(bool(search(regex, 'DHSJdhjsU')), False)
        self.assertEqual(bool(search(regex, 'fjd3IR9.;')), False)
        self.assertEqual(bool(search(regex, 'fjd3  IR9')), False)
        self.assertEqual(bool(search(regex, 'djI38D55')), True)
        self.assertEqual(bool(search(regex, 'a2.d412')), False)
        self.assertEqual(bool(search(regex, 'JHD5FJ53')), False)
        self.assertEqual(bool(search(regex, '!fdjn345')), False)
        self.assertEqual(bool(search(regex, 'jfkdfj3j')), False)
        self.assertEqual(bool(search(regex, '123')), False)
        self.assertEqual(bool(search(regex, 'abc')), False)
        self.assertEqual(bool(search(regex, '123abcABC')), True)
        self.assertEqual(bool(search(regex, 'ABC123abc')), True)
        self.assertEqual(bool(search(regex, 'Password123')), True)

def main():
    unittest.main()

if __name__=="__main__":
    main()

