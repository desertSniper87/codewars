from itertools import permutations as p

def listPosition(word):
    for ix, i in enumerate(sorted(set(p(word)))):
        if i == tuple(word):                                                                                     
            return ix + 1
