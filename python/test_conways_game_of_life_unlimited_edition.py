#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 24.07.2018
# Last Modified Date: 24.07.2018

import unittest
from conways_game_of_life_unlimited_edition import *

def htmlize(array):
    s = []
    for row in array:
        for cell in row:
            s.append('▓▓' if cell else '░░')
        s.append('<:LF:>')
    return ''.join(s)

start = [[1,0,0],
         [0,1,1],
         [1,1,0]]
end   = [[0,1,0],
         [0,0,1],
         [1,1,1]]
         
class TestConway(unittest.TestCase):
    def test_draw(self):
        print('Glider<:LF:>' + htmlize(start) + 'Glider 1')

        resp = get_generation(start, 1)
        self.assertEqual(resp, end, 'Got<:LF:>' + htmlize(resp) + '<:LF:>instead of<:LF:>' + htmlize(end))

def main():
    unittest.main()
    
if __name__ == '__main__':
    main()
