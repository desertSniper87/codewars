#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 27.01.2018
# Last Modified Date: 28.01.2018
# Completed         : 27.01.2018
def cakes(recipe, available):
    # TODO: insert code
    req = {}
    for i in recipe:
        # print(i)
        if i not in available:
            return 0
        req[i] = available[i]/recipe[i]

        a = min(req, key=req.get)
    # print(req[a])
    return int(req[a])

if __name__ == "__main__":
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe, available))

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe, available))
