#!/usr/bin/python3
"""N Queens Solver: Solves the N Queens problem."""
import sys


if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def solve_n_queens(size):
    """
    Places N non-attacking queens on an NxN chessboard.
    """
    visited_cols, visited_pos_diag, visited_neg_diag = set(), set(), set()
    current_board = [[] for _ in range(size)]
    solved_boards = []

    def backtrack(row):
        """
        Tool for solving constraint satisfaction problems.
        """
        if row == size:
            copy_of_board = current_board.copy()
            solved_boards.append(copy_of_board)
            return

        for col in range(size):
            if (col in visited_cols
                    or (row + col) in visited_pos_diag or
                    (row - col) in visited_neg_diag):
                continue

            visited_cols.add(col)
            visited_pos_diag.add(row + col)
            visited_neg_diag.add(row - col)

            current_board[row] = [row, col]

            backtrack(row + 1)

            visited_cols.remove(col)
            visited_pos_diag.remove(row + col)
            visited_neg_diag.remove(row - col)
            current_board[row] = []

    backtrack(0)

    return solved_boards


if __name__ == "__main__":
    boards = solve_n_queens(n)
    for board in boards:
        print(board)
