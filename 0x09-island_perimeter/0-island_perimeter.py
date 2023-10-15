#!/usr/bin/python3
"""
Module calculates the perimeter of an island
"""


def island_perimeter(grid):
    """
    island perimter
    """
    perimeter = 0
    rows = len(grid)
    cur_cols = len(grid[0])

    for row in range(rows):
        for col in range(cur_cols):
            if grid[row][col] == 1:
                perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2
    return perimeter
