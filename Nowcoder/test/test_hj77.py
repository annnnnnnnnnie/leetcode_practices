import unittest
import Nowcoder.src.hj77_trains_entering_station as solution


class MyTestCase(unittest.TestCase):

    def test_can_recognize_valid_sequence_one(self):
        trains = [1, 2, 3]
        seq = [1, 2, 3]
        self.assertTrue(solution.is_valid_sequence(seq, trains))

    def test_can_recognize_valid_sequences(self):
        seqs = [[1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 2, 1]]
        for seq in seqs:
            trains = [1, 2, 3]
            self.assertTrue(solution.is_valid_sequence(seq, trains))

    def test_can_recognize_invalid_sequence_one(self):
        bad_seq = [3, 1, 2]
        trains = [1, 2, 3]
        self.assertFalse(solution.is_valid_sequence(bad_seq, trains))


if __name__ == '__main__':
    unittest.main()
