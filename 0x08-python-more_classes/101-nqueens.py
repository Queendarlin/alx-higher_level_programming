#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Checks if a queen can be placed safely at the given position."""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col):
    """Recursively solves the N queens problem using backtracking."""
    if col >= N:
        print(board)
        return

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1)
            board[i][col] = 0  # Backtrack


def solve_n_queens(N):
    """Main function to solve the N queens problem."""
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_n_queens_util(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    solve_n_queens(N)
