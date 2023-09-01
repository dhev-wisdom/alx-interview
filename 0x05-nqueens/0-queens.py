#!/usr/bin/python3
"""
Module arranges Queens on a Chess board using Backtracking algorithm
"""

import sys


def is_safe(board, row, col, N):
    """
    function checks if Queen can rightly fit in this position
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    return True


def solveNQueensUtil(board, row, N, solutions):
    """
    method
    """
    if row == N:
        solutions.append([[i, board[i].index(1)] for i in range(N)])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solveNQueensUtil(board, row + 1, N, solutions)
            board[row][col] = 0


def solveNQueens(N):
    """
    main
    """
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [[0] * N for _ in range(N)]
    solutions = []
    solveNQueensUtil(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solveNQueens(N)
