import unittest

from Beginner.x2f9gg import x2f9gg


class TestCheckRow(unittest.TestCase):
    def setUp(self) -> None:
        self.check_row = x2f9gg.check_row

    def test_all_blank(self):
        row = ["."] * 9
        result = self.check_row(row)
        self.assertTrue(result)

    def test_all_unique(self):
        row = [str(i) for i in range(1, 10)]
        result = self.check_row(row)
        self.assertTrue(result)

    def test_all_same(self):
        row = ["6"] * 9
        result = self.check_row(row)
        self.assertFalse(result)


BOARD_GOOD = \
    [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

# board[0][1] changed from "3" to "5"
BOARD_BAD = \
    [["5", "5", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


class TestCheckBlock(unittest.TestCase):
    def setUp(self) -> None:
        self.check_block = x2f9gg.check_block
        self.check_all_blocks = x2f9gg.check_all_blocks

    def test_positive_one_block_case(self):
        board = BOARD_GOOD
        start_row = 0
        start_col = 0
        result = self.check_block(board, start_row, start_col)
        self.assertTrue(result)

    def test_negative_one_block_case(self):
        board = BOARD_BAD
        start_row = 0
        start_col = 0
        result = self.check_block(board, start_row, start_col)
        self.assertFalse(result)

    def test_positive_check_all_blocks(self):
        board = BOARD_GOOD
        result = self.check_all_blocks(board)
        self.assertTrue(result)

    def test_negative_check_all_blocks(self):
        board = BOARD_BAD
        result = self.check_all_blocks(board)
        self.assertFalse(result)


class TestOverall(unittest.TestCase):
    def setUp(self) -> None:
        self.check_sudoku = x2f9gg.is_valid_sudoku

    def test_positive_case(self):
        board = BOARD_GOOD
        result = self.check_sudoku(board)
        self.assertTrue(result)

    def test_negative_case(self):
        board = BOARD_BAD
        result = self.check_sudoku(board)
        self.assertFalse(result)
