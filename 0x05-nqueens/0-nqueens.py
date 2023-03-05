#!/usr/bin/python3
"""Solving N Queens Problem using backtracking"""
import sys


def printSolution(board, n):
    """Print allocated positions to the queen"""
    for r in range(n):
        for c in range(n):
            if c == board[r]:
                print(board[r][c], end = " ")


def is_safe_position(board, r, c, row):
    """Checks if the position is safe for the queen"""
    return board[i] in (c, c - r + row, r - row + c)


def safe_positions(board, row, n):
    """Find all safe positions where the queen can be allocated"""
    if row == n:
        printSolution(board, n)

    else:
        for c in range(n):
            allowed = True
            for r in range(row):
                if is_safe_position(board, c, r, row):
                    allowed = False
            if allowed:
                board[row] = j
                safe_positions(board, row + 1, n)


def create_board(size):
    """Fill the board with 0"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
safe_positions(board, row, int(n))
