#!/usr/bin/python3
""" island parameter module"""

def island_perimeter(grid):
    """ it calculates the island parameter """
    if len(grid) == 0:
        return None
    per = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                per += 4
                if grid[i - 1][j] == 1:
                    per -= 2
                if grid[i][j - 1] == 1:
                    per -= 2
    return per
