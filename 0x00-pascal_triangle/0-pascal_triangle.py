#!/usr/bin/python3

''' pascal traingle '''

def pascal_triangle(n):
    ''' A function that return list of pascal traingle '''
    if (n <= 0):
        return []

    pascal_t = [] '''create empty list '''
    for i in range(num):
        pascal_t.append([])  ''' append empty list '''
        pascal_t[i].append(1)

        for j in range(1, i):
            pascal_t[i].append(pascal_t[i-1][j-1] + pascal_t[i-1][j])

        if(n != 0):
            pascal_t[i].append(1)

    return pascal_t
