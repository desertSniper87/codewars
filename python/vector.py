#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 30.01.2018
# Last Modified Date: 31.01.2018
# Completed         : 31.01.2018
class Vector:

    """Docstring for Vector. """
    values = []

    # def __init__(self):
        # """TODO: to be defined1. """
        # __init__(self)

    def __str__(self):
        # result='('
        # for i in self.values:
            # result.append(i)

        x = str(tuple(self.values)).replace(' ', '')
        return x

    def __init__(self, val):
        self.values = val

    def add(self, a):
        if len(self.values)!=len(a.values):
            raise ValueError
        result = []
        for i, j in zip(self.values, a.values):
            result.append(i+j)

        return Vector(result)

    def equals(self, a):
        return self.values == a.values

    def subtract(self, a):
        if len(self.values)!=len(a.values):
            raise ValueError
        result = []
        for i, j in zip(self.values, a.values):
            result.append(i-j)

        return Vector(result)

    def dot(self, a):
        if len(self.values)!=len(a.values):
            raise ValueError
        result = 0
        for i, j in zip(self.values, a.values):
            result+=i*j

        return result

    def norm(self):
        result = 0
        for i in self.values:
            result+=i**2

        return (result**0.5)

if __name__ == "__main__":
    a = Vector([1, 2, 3])
    b = Vector([3, 4, 5]) 

    # print(a.add(b))
    # print(a.dot(b))
    print(a.norm())

    # print(a.__str__)
