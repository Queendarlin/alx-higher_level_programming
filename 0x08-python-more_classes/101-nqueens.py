#!/usr/bin/python3
import sys


def print_solution(board):
    """
    Prints the solution in the required format.
    """
    for row, col in enumerate(board):
        print("[{}, {}]".format(row, col), end="")
        if row != len(board) - 1:
            print(", ", end="")
    print()


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at the given position.
    """
    for prev_row, prev_col in enumerate(board):
        if prev_col == col or \
                prev_row + prev_col == row + col or \
                prev_row - prev_col == row - col:
            return False
    return True


def solve_nqueens(board, row, n):
    """
    Recursive function to solve N Queens problem.
    """
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n)
            board[row] = 0


def nqueens(n):
    """
    Main function to solve N Queens problem.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [0] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
