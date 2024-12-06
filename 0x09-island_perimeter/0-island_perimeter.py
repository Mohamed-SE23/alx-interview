#!/usr/bin/python3
"""
This is a script that returns the perimeter of the
island described in grid argument.

args:
    grid: is a list of integers, 0 represent water and
          1 represent land
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.

    args:
        grid (list of list of int): A rectangular grid where:
                                    - 0 represents water.
                                    - 1 represents land.
                                    - Cells are connected
                                      horizontally/vertically.

    Returns:
        int: The perimeter of the island.

    Assumptions:
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island does not have "lakes".
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                cell_perimeter = 4
                if r > 0 and grid[r - 1][c] == 1:
                    cell_perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:
                    cell_perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:
                    cell_perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:
                    cell_perimeter -= 1
                perimeter += cell_perimeter
    return perimeter
