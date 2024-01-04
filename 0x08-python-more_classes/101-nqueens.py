#!/usr/bin/python3
"""The N-queens puzzle"""

import sys


def initialize_chessboard(size):
    """Initialize an `size`x`size` sized chessboard with 0's."""
    chessboard = []
    [chessboard.append([]) for i in range(size)]
    [row.append(' ') for i in range(size) for row in chessboard]
    return chessboard


def deepcopy_chessboard(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(deepcopy_chessboard, chessboard))
    return chessboard


def get_queen_positions(chessboard):
    """Return the list of lists representation of queen positions in a chessboard."""
    positions = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                positions.append([r, c])
                break
    return positions


def mark_spots(chessboard, row, col):
    """Mark spots on a chessboard."""
    # Mark out all forward spots
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"
    # Mark out all backward spots
    for c in range(col - 1, -1, -1):
        chessboard[row][c] = "x"
    # Mark out all spots below
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"
    # Mark out all spots above
    for r in range(row - 1, -1, -1):
        chessboard[r][col] = "x"
    # Mark out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    # Mark out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # Mark out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solution(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(chessboard):
        solutions.append(get_queen_positions(chessboard))
        return solutions

    for c in range(len(chessboard)):
        if chessboard[row][c] == " ":
            tmp_chessboard = deepcopy_chessboard(chessboard)
            tmp_chessboard[row][c] = "Q"
            mark_spots(tmp_chessboard, row, c)
            solutions = recursive_solution(tmp_chessboard, row + 1,
                                           queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chessboard = initialize_chessboard(int(sys.argv[1]))
    solutions = recursive_solution(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
