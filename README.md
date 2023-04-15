# Sudoku-solver

This is a sudoku solver code written in python

## Description

1. Input: List of Lists, where each inner list is a row in sudoku puzzle, 9-by-9 puzzle
2. "-1" represents empty cell
3. Other values can be from 1 to 9

4. Sample input
```
[
    [8, 2, -1,   5, -1, -1,   3, 6, -1],
    [-1, -1, -1,   -1, -1, 9,   -1, 5, -1],
    [7, -1, -1,   -1, -1, -1,   -1, -1, -1],

    [-1, -1, 6,   -1, -1, -1,   -1, -1, -1],
    [5, 3, -1,   9, -1, -1,   8, -1, -1],
    [-1, -1, -1,   -1, 4, -1,   -1, -1, 1],

    [-1, -1, 7,   2, -1, -1,   -1, -1, -1],
    [2, 6, -1,   -1, -1, 1,   -1, -1, 8],
    [-1, -1, 9,   -1, -1, -1,   6, -1, -1]
]
```