import itertools
from typing import List

# board[i] is the i-th row, with the top row being board[0] and the bottom row being board[8]
# board[_][j] is the j-th col, with the left-most being board[_][0] and the right-most being board[_][8]
PLACE_HOLDER = '.'

BOARD_SIZE = 9
BLOCK_SIZE = 3


# Checks if this row is legal (no duplicate numbers)
def check_row(row):
    numbers = list(map(lambda c: int(c), filter(lambda c: c.isdigit(), row)))
    return len(numbers) == len(set(numbers))


# Checks if this block is legal (no duplicate numbers)
def check_block(board, start_row, start_col):
    row = []
    for i in range(BOARD_SIZE // BLOCK_SIZE):
        for j in range(BOARD_SIZE // BLOCK_SIZE):
            row.append(board[start_row + i][start_col + j])
    return check_row(row)


def check_all_blocks(board):
    results = []
    for start_row in range(0, BOARD_SIZE, BLOCK_SIZE):
        for start_col in range(0, BOARD_SIZE, BLOCK_SIZE):
            result_for_one_block = check_block(board, start_row, start_col)
            results.append(result_for_one_block)
    result = all(results)
    return result


def check_col(board, col_number):
    row = []
    for row_number in range(BOARD_SIZE):
        row.append(board[row_number][col_number])
    return check_row(row)


def check_all_rows(board):
    results = []
    for row_number in range(BOARD_SIZE):
        result_one_row = check_row(board[row_number])
        results.append(result_one_row)
    return all(results)


def check_all_cols(board):
    results = []
    for col_number in range(BOARD_SIZE):
        result_one_col = check_col(board, col_number)
        results.append(result_one_col)
    return all(results)


def is_valid_sudoku(board):
    return all([check_all_rows(board), check_all_cols(board), check_all_blocks(board)])


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return is_valid_sudoku(board)
