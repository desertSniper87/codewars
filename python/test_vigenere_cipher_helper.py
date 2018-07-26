from vignere_cipher_helper import *

import unittest

class VigenereCipherTest(unittest.TestCase):
    def test_create_cipher(self):
        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"

        c = VigenereCipher(key, abc)

    def test_encode(self):

        abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = "LEMON"
        c = VigenereCipher(key, abc)

        plainText = 'A'
        ciphertext = 'L'

        self.assertEqual(c.encode(plainText), ciphertext)

        plainText = 'ATTACKATDAWN'
        ciphertext = 'LXFOPVEFRNHR'

        self.assertEqual(c.encode(plainText), ciphertext)

        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"

        c = VigenereCipher(key, abc)

        self.assertEqual(c.encode('codewars'), 'rovwsoiv')
        self.assertEqual(c.encode('waffles'), 'laxxhsj')
        self.assertEqual(c.encode('CODEWARS'), 'CODEWARS')

        c = VigenereCipher('カタカナ', 'アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー')
        self.assertEqual(c.decode('ドオカセガヨゴザキアニ'),'ドモアリガトゴザイマス')

    def test_decodedescription(self):
        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"
        c = VigenereCipher(key, abc)

        self.assertEqual(c.decode('rovwsoiv'), 'codewars')
        self.assertEqual(c.decode('laxxhsj'), 'waffles')
        self.assertEqual(c.decode('CODEWARS'), 'CODEWARS')
        
        

def main():
        unittest.main()

if __name__ == "__main__":
    main()
            


