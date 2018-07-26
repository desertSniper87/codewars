from caesar_cipher_helper import *

import unittest

class CaesarCipherTest(unittest.TestCase):
    def test_create_cipher(self):
        c = CaesarCipher(5)
        self.assertEqual(len(c.alphaSet), 26)
        
    def test_encode(self):
        c = CaesarCipher(5)
        # self.assertEqual(c.encode("Codewars"), "HTIJBFWX")
        self.assertEquals(c.encode("IT'S A SHIFT CIPHER!!"), "NY'X F XMNKY HNUMJW!!");

    def test_decode(self):
        c = CaesarCipher(5)
        self.assertEqual(c.decode("HTIJBFWX"), 'CODEWARS');

def main():
        unittest.main()

if __name__ == "__main__":
    main()
        


