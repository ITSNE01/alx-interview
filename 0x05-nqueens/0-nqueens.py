#!/usr/bin/python3
"""
Solve the N queens problem: place N non-attacking queens on an N×N chessboard.
Usage: nqueens N
"""
import sys


def solve_nqueens(n):
    """
    Generate all solutions for the N queens problem.

    Returns:
        List of solutions, where each solution is a list of [row, col] pairs.
    """
    solutions = []
    queens = []  # queens[row] = col

    def backtrack(row):
        if row == n:
            solutions.append([[r, c] for r, c in enumerate(queens)])
            return
        for col in range(n):
            valid = True
            for r, c in enumerate(queens):
                if c == col or abs(c - col) == abs(r - row):
                    valid = False
                    break
            if not valid:
                continue
            queens.append(col)
            backtrack(row + 1)
            queens.pop()

    backtrack(0)
    return solutions


def main():
    if len(sys.argv) != 2:
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

    for solution in solve_nqueens(n):
        print(solution)


if __name__ == '__main__':
    main()
