#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 28.01.2018
# Last Modified Date: 28.01.2018

# import itertools

# def flatten(listOfLists):
    # "Flatten one level of nesting"
    # return chain.from_iterable(listOfLists)
import math

def s1(array):
    """TODO: Docstring for s1.

    :array: TODO
    :returns: TODO

    """
    dim = int(math.sqrt(len(array)))
    # print(dim)
    result = array[0:dim]
    # print(array)
    # print(result)
    # print("array, array[dim:]", array, array[dim:])
    # for index_i, i in enumerate(array[dim:]):
    for index_i, i in enumerate(array[dim:], start=dim):
        print("i ,index_i",i ,index_i)
        if (index_i%dim == 0):
            result.append(i)
            # print("array[index_i], i, index_i", array[index_i], i, index_i)
            # del array[index_i]
            # print("array", array)
            # print(result)
    # array = array[dim:]
    # print(array)
    print(result)
    return result, array
        # if ()


def snail(array):
    # l = flatten(array)
    flat = [x for sublist in array for x in sublist]
    # print(flat)
    result = []
    while(flat!=[]):
        r, flat = s1(flat)
        # print(flat)
        result.append(r)
        # print(result)

        
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
