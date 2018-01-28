#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 28.01.2018
# Last Modified Date: 28.01.2018

# import itertools

# def flatten(listOfLists):
    # "Flatten one level of nesting"
    # return chain.from_iterable(listOfLists)

def snail(array):
    # l = flatten(array)
    flat = [x for sublist in nested for x in sublist]
    # result = []
    # for a in array:
        # # for index_i, i in enumerate(a):
        # print(a)
        # for i in reversed(a):
            # # print(index_i, i)
            # result.append(a.pop(0))
            # print(a, result)
        # result.append(a[-1])
        # a.pop(-1)
            # print(i)
        # print(result)

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array)


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
