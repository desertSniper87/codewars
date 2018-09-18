import numpy
from math import ceil

def determinant(matrix):
    dimension = len(matrix)

    # for ix, i in enumerate(matrix):
    #     for jx, j in enumerate(i):
    #         print(ix, jx, i, j)

    return ceil(numpy.linalg.det(matrix))
