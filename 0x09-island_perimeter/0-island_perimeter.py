#!/usr/bin/python3
"""
Calculate the perimeter of a single island in a 2D grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D map where 1 represents land and
            0 represents water. The grid is surrounded by water and has
            exactly one island without lakes.

    Returns:
        int: the perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check above
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check below
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
