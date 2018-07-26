import unittest
from paginationHelper import *

class paginationHelperTest(unittest.TestCase):
    def test_createHelper(self):
        collection = range(1,25)
        helper = PaginationHelper(collection, 10)

    def test_page_count(self):
        collection = range(1,25)
        helper = PaginationHelper(collection, 10)
        self.assertEqual(helper.page_count(), 3, 'page_count is returning incorrect value.')
       
    def test_page_index(self):
        collection = range(1,25)
        helper = PaginationHelper(collection, 10)
        self.assertEqual(helper.page_index(23), 2, 'page_index returned incorrect value')
        self.assertEqual(helper.page_index(24), -1, 'page_index returned incorrect value')
        self.assertEqual(helper.page_index(3), 0, 'page_index returned incorrect value')

        collection = []
        helper = PaginationHelper(collection, 10)
        self.assertEqual(helper.page_index(0), 2, 'page_index returned incorrect value')
        
    def test_item_count(self):
        collection = range(1,25)
        helper = PaginationHelper(collection, 10)
        self.assertEqual(helper.item_count(), 24, 'item_count returned incorrect value')

    def test_page_item_count(self):
        collection = range(1,25)
        helper = PaginationHelper(collection, 10)
        self.assertEqual(helper.page_item_count(1), 10, 'item_count returned incorrect value')
        self.assertEqual(helper.page_item_count(2), 4, 'item_count returned incorrect value')
        # self.assertEqual(helper.page_item_count(4), 4, 'item_count returned incorrect value')
        

        

    # def test_create_cipher(self):
        # abc = "abcdefghijklmnopqrstuvwxyz"
        # key = "password"

        # c = VigenereCipher(key, abc)

    # def test_encode(self):

        # abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        # key = "LEMON"
        # c = VigenereCipher(key, abc)

        # plainText = 'A'
        # ciphertext = 'L'

        # self.assertEqual(c.encode(plainText), ciphertext)

        # plainText = 'ATTACKATDAWN'
        # ciphertext = 'LXFOPVEFRNHR'

        # self.assertEqual(c.encode(plainText), ciphertext)

        # abc = "abcdefghijklmnopqrstuvwxyz"
        # key = "password"

        # c = VigenereCipher(key, abc)

        # self.assertEqual(c.encode('codewars'), 'rovwsoiv')
        # self.assertEqual(c.encode('waffles'), 'laxxhsj')
        # self.assertEqual(c.encode('CODEWARS'), 'CODEWARS')

        # c = VigenereCipher('カタカナ', 'アイウエオァィゥェォカキクケコサシスセソタチツッテトナニヌネノハヒフヘホマミムメモヤャユュヨョラリルレロワヲンー')
        # self.assertEqual(c.decode('ドオカセガヨゴザキアニ'),'ドモアリガトゴザイマス')

    # def test_decodedescription(self):
        # abc = "abcdefghijklmnopqrstuvwxyz"
        # key = "password"
        # c = VigenereCipher(key, abc)

        # self.assertEqual(c.decode('rovwsoiv'), 'codewars')
        # self.assertEqual(c.decode('laxxhsj'), 'waffles')
        # self.assertEqual(c.decode('CODEWARS'), 'CODEWARS')
        
        

def main():
        unittest.main()

if __name__ == "__main__":
    main()
            


