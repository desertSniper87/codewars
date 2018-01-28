#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 28.01.2018
# Last Modified Date: 28.01.2018
"""https://www.codewars.com/kata/ordered-count-of-characters/train/python"""

def ordered_count(input):
    word_list = []
    words = []
    for i in input:
        x = input.count(i)
        if i not in words:
            word_tup = (i, x)
            word_list.append(word_tup)
            words.append(i)
    print(word_list)

ordered_count('abracadabra')

