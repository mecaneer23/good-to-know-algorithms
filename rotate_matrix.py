#!/usr/bin/env python3
"""A couple different ways to rotate a matrix 90 degrees clockwise"""

from typing import Any, TypeVar

T = TypeVar("T")


def print_matrix(matrix: list[list[Any]]) -> None:
    """Print out a 2d list (matrix)"""
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()
    print()


def just_loops(matrix: list[list[int]]) -> list[list[int]]:
    """
    Other than generating the 2d new_matrix pythonically,
    this function uses an algorithm which should be viable
    in any procedural language.

    Uses int because there is no way to get a default of
    type T in python yet.
    """
    new_matrix: list[list[int]] = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for row_ptr, row in enumerate(matrix):
        for col_ptr, _ in enumerate(row):
            new_matrix[col_ptr][row_ptr] = matrix[(-row_ptr + len(row) - 1) % len(row)][col_ptr]
    return new_matrix


def with_zip(matrix: list[list[T]]) -> list[list[T]]:
    """Pretty Pythonic way of rotating a list of lists"""
    return list(zip(*matrix[::-1]))


def main():
    """Run all of the algoritms"""
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    print_matrix(matrix)
    print_matrix(just_loops(matrix))
    print_matrix(with_zip(matrix))


if __name__ == "__main__":
    main()
