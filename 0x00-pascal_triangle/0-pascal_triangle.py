#!/usr/bin/python3
"""Pascal Triangle Interview Challenge"""


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_t = []

    for i in range(n):
        pascal_t.append([])
        pascal_t[i].append(1)

        for j in range(1, i):
            x = pascal_t[i-1][j-1]
            y = pascal_t[i-1][j]
            pascal_t[i].append(x+y)

        if(n != 0 and i != 0):
            pascal_t[i].append(1)

    return pascal_t
