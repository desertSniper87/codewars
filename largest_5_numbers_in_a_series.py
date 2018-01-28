#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 27.01.2018
# Last Modified Date: 28.01.2018
# Completed         : 27.01.2018

def solution(digits):
    l = [int(i) for i in str(digits)]
    maxi = 0
    i = 0
    while(i<len(l)-4):
        number = 0
        base = 1
        for index_j, j in enumerate(reversed(l[i:i+5])):
            number+=base*j
            base *= 10
        if (number>maxi):
            maxi = number
        elif(number==99999):
            return number
        i+=1

    return maxi

if __name__ == "__main__":
    x = solution(1234567890)
    print(x)
