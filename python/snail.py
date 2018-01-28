#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 28.01.2018
# Last Modified Date: 29.01.2018
# Completed         : 29.01.2018

import math

def s1(array):
    print(array)
    """TODO: Docstring for s1.

    :array: TODO
    :returns: TODO

    """
    dim = int(math.sqrt(len(array)))
    result = array[0:dim]
    for index_i, i in enumerate(array[dim:], start=dim):
        if ((index_i+1)%dim == 0):
            result.append(i)
    return result, [i for i in array if i not in result][::-1]


def snail(array):
    flat = [x for sublist in array for x in sublist]
    result = []
    while(flat!=[]):
        r, flat = s1(flat)
        result.extend(r)
    print(result)
    return result

        
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]


array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array)
