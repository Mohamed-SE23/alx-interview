#!/usr/bin/python3
"""
A function that rotate a given matrix.
"""


def rotate_2d_matrix(matrix):
    """
    This function rotate the matrix in args.

    Args:
        matrix: an array of elements.

    Returns:
        its only rotate the matrix in the args and
        no returned value.
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
