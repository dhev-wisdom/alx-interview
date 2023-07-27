#!/usr/bin/python3
"""
Module defines a function that creates Pascal triangle(s)
"""

def pascal_triangle(n):
    """
    Pascal triangle:
    returns a list of lists of integers
    representing the Pascal’s triangle of n:
    """

    if n <= 0:
        return []

    pascal = []
    row = []
    num_to_add = 1
    level = 1

    for a in range(n):
        index1 = 0
        index2 = 1
        end_b = False
        last_list = []

        if a >= 2:
            last_list = pascal[-1]

        for b in range(level):
            if b < 1 or level <= 2:
                pass
            elif b >= 1 and (len(last_list) > index2):
                num_to_add = last_list[index1] + last_list[index2]
            else:
                num_to_add = 1

            row.append(num_to_add)

            try:
                last_list[index2]
            except IndexError:
                end_b = True

            if a >= 2 and b > 0 and end_b is False:
                index1 += 1
                index2 += 1

        level += 1
        pascal.append(row)
        row = []

    return pascal
