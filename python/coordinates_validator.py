#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 29.01.2018
# Last Modified Date: 29.01.2018


def is_valid_coordinates(coordinates):
    """TODO: Docstring for is_valid_coordinates.

    :coordinates: TODO
    :returns: TODO

    """
    # for i in coordinates:
    # print(i)
    print(coordinates)
    coords = coordinates.split(', ') 
    try:
        for j in coords:
            if 'e' in j:
               return ("False")
        coord = float(coords[0])
        if coord<-90 or coord>90:
            return False
        coord = float(coords[1])
        if coord<-180 or coord>180:
            return False
    except:
        print("False")
        return False

    print("True")
    return True



    # print(x)

    # coord = 

if __name__ == "__main__":
    valid_coordinates = [
                         "-23, 25",
                         "4, -3",
                         "24.53525235, 23.45235",
                         "04, -23.234235",
                         "43.91343345, 143"
                        ] 
    for i in valid_coordinates:
        print(i)
        is_valid_coordinates(i)

    invalid_coordinates = [
        "23.234, - 23.4234",
        "2342.43536, 34.324236",
        "N23.43345, E32.6457",
        "99.234, 12.324",
        "6.325624, 43.34345.345",
        "0, 1,2",
        "0.342q0832, 1.2324",
        "23.245, 1e1"
    ]

    for i in invalid_coordinates:
        print(i)
        is_valid_coordinates(i)
