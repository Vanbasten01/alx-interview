#!/usr/bin/python3
"""  Rotate 2D Matrix """


def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix clockwise in place."""
    n = len(matrix[0])

    for i in range((n + 1) // 2):
        for j in range(n // 2):
            temp = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = temp
