from pprint import pprint
from typing import List


def find_next_empty_cell(sudoku_puzzle: List[List[int]]):
    """
    This function finds the next empty cell in the Sudoku puzzle.

    Args:
        sudoku_puzzle (list): A 2D array of integers representing the Sudoku puzzle.

    Returns:
        The row and column indices of the next empty cell,
        or None, None -> if there are no empty cells left.
    """
    # keep in mind that we are using 0-8 for our indices
    for row in range(9):
        for column in range(9): # range(9) is 0, 1, 2, ... 8
            if sudoku_puzzle[row][column] == -1:
                return row, column

    return None, None  # if no spaces in the puzzle are empty (-1)

def is_valid(sudoku_puzzle: List[List[int]], guess_input: int, row_num: int, col_num: int):
    """
    This function checks if a number can be placed in a given cell of the Sudoku puzzle.

    Args:
        sudoku_puzzle (list): A 2D array of integers representing the Sudoku puzzle.
        guess_input (int): The number to check.
        row_num (int): The row index of the cell to check.
        col_num (int): The column index of the cell to check.

    Returns:
        True if the number can be placed in the cell, False otherwise.
    """

    # Check if the number is already in the same row.
    row_val = sudoku_puzzle[row_num]
    if guess_input in row_val:
        return False # if we've repeated, then our guess is not valid!

    # Check if the number is already in the same column.
    col_val = [sudoku_puzzle[i][col_num] for i in range(9)]
    if guess_input in col_val:
        return False

     # Check if the number is already in the same 3x3 box.
    row_start = (row_num // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col_num // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if sudoku_puzzle[r][c] == guess_input:
                return False

    return True

def solve_sudoku(sudoku_puzzle: List[List[int]]):
    """
    This function solves a Sudoku puzzle using backtracking.

    Args:
        sudoku_puzzle (list): A 2D array of integers representing the Sudoku puzzle.

    Returns:
        A 2D array of integers representing the solved Sudoku puzzle.
    """
    
    # Find the next empty cell in the puzzle.
    row, col = find_next_empty_cell(sudoku_puzzle)

    # If there are no empty cells left, the puzzle is solved.
    if row is None: 
        return True 
    
    # Try filling the empty cell with a number.
    for guess_num in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
        if is_valid(sudoku_puzzle, guess_num, row, col):
            # Recursively solve the rest of the puzzle.
            sudoku_puzzle[row][col] = guess_num
            # step 4: then we recursively call our solver!
            if solve_sudoku(sudoku_puzzle):
                return True
        
        # If the recursion doesn't produce a valid solution, backtrack.
        sudoku_puzzle[row][col] = -1

    # If no number works in the empty cell, the puzzle is unsolvable.
    return False

if __name__ == '__main__':
    example_board = [
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
    print(solve_sudoku(example_board))
    pprint(example_board)