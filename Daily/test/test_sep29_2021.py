import unittest

from Daily.src.sep29_2021 import apply_moves, is_done, Move, combine_move, find_min_moves


class TestHelperFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.is_done = is_done
        self.combine_move = combine_move

    def test_done_is_done(self):
        machines = [3, 3, 3]
        avg = 3
        result = self.is_done(machines, avg)
        self.assertTrue(result)

    def test_not_done_is_not_done(self):
        machines = [3, 5, 3]
        avg = 4
        result = self.is_done(machines, avg)
        self.assertFalse(result)

    def test_apply_moves_correctly(self):
        machines = [3, 6, 3]

        moves_1 = [Move.STAY, Move.LEFT, Move.STAY]
        apply_moves(machines, moves_1)
        answer_1 = [4, 5, 3]
        self.assertListEqual(answer_1, machines)

        moves_2 = [Move.STAY, Move.RIGHT, Move.STAY]
        apply_moves(machines, moves_2)
        answer_2 = [4, 4, 4]
        self.assertListEqual(answer_2, machines)

    def test_combine_moves_properly(self):
        m1 = Move.STAY
        m2 = Move.LEFT
        m3 = Move.RIGHT

        self.assertEqual(Move.LEFT, combine_move(m1, m2))
        self.assertEqual(Move.RIGHT, combine_move(m1, m3))
        self.assertEqual(Move.STAY, combine_move(m1, m1))
        self.assertEqual(Move.BOTH, combine_move(m2, m3))


class TestFindMinMoves(unittest.TestCase):
    def setUp(self) -> None:
        self.find_min_moves = find_min_moves

    def test_simple_case_1(self):
        machines = [2, 4, 3]
        result = self.find_min_moves(machines)
        answer = 1
        self.assertEqual(answer, result)

    def test_simple_case_2(self):
        machines = [3, 4, 2]
        result = self.find_min_moves(machines)
        answer = 1
        self.assertEqual(answer, result)

    def test_simple_case_3(self):
        machines = [4, 3, 2]
        result = self.find_min_moves(machines)
        answer = 1
        self.assertEqual(answer, result)

    def test_simple_impossible_case_1(self):
        machines = [4, 3, 3]
        result = self.find_min_moves(machines)
        answer = -1
        self.assertEqual(answer, result)

    def test_two_moves_case_1(self):
        machines = [2, 5, 2]
        result = self.find_min_moves(machines)
        answer = 2
        self.assertEqual(answer, result)

    def test_given_simple_case_1(self):
        machines = [1, 0, 5]
        result = self.find_min_moves(machines)
        answer = 3
        self.assertEqual(answer, result)

    def test_given_wrong_case_1(self):
        machines = [3, 1, 0, 4]
        result = self.find_min_moves(machines)
        answer = 2
        self.assertEqual(answer, result)

    def test_given_wrong_case_2(self):
        machines = [100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0, 100000, 0]
        result = self.find_min_moves(machines)
        answer = 100000 / 2
        self.assertEqual(answer, result)

    def test_given_ot_case_2(self):
        machines = [1, 0, 5]
        result = self.find_min_moves(machines)
        answer = 3
        self.assertEqual(answer, result)

    def test_edge_case_1(self):
        machines = [0]
        result = self.find_min_moves(machines)
        answer = 0
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
