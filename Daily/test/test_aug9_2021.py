import unittest

from Daily.src import aug9_2021


class TestGenerateUglySeq(unittest.TestCase):
    def setUp(self) -> None:
        self.seq_generator = aug9_2021.generate_super_ugly_sequence

    def test_generate_short_seq(self):
        n = 3
        sorted_primes = [2, 3]
        result = self.seq_generator(n, sorted_primes)
        answer = [1, 2, 3]
        self.assertListEqual(answer, result)

    def test_generate_short_seq_case2(self):
        n = 12
        sorted_primes = [2, 7, 13, 19]
        result = self.seq_generator(n, sorted_primes)
        answer = [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
        self.assertListEqual(answer, result)
