import heapq
import unittest

from Daily.src import aug9_2021


class TestGenerateUglySeq(unittest.TestCase):
    def setUp(self) -> None:
        self.seq_generator = aug9_2021.generate_super_ugly_sequence_heap

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


class TestOverall(unittest.TestCase):
    def setUp(self) -> None:
        self.test_subject = aug9_2021.nth_super_ugly_number

    def test_small_case(self):
        n = 1
        primes = [2, 3, 5]
        result = self.test_subject(n, primes)
        answer = 1
        self.assertEqual(answer, result)

    def test_medium_case(self):
        n = 12
        primes = [2, 7, 13, 19]
        result = self.test_subject(n, primes)
        answer = 32
        self.assertEqual(answer, result)

    def test_large_case(self):
        n = 100000
        primes = [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181,
                  199, 211,
                  229, 233, 239, 241, 251]
        result = self.test_subject(n, primes)
        answer = 1092889481
        self.assertEqual(answer, result)


class TestPotentialCombClass(unittest.TestCase):
    def setUp(self) -> None:
        self.sorted_primes = [2, 5]

    def test_less_than(self):
        result = [1, 2]
        comb_1 = aug9_2021.PotentialCombination(0, self.sorted_primes, result)
        comb_2 = aug9_2021.PotentialCombination(1, self.sorted_primes, result)
        self.assertTrue(comb_1 < comb_2)

    def test_less_than_case_2(self):
        result = [1, 2]
        comb_1 = aug9_2021.PotentialCombination(0, self.sorted_primes, result)
        comb_2 = aug9_2021.PotentialCombination(1, self.sorted_primes, result)
        comb_1.next_comb()
        self.assertLess(comb_2, comb_1)

    def test_works_with_heapq(self):
        comb_heap = []
        result = [1, 2]
        comb_1 = aug9_2021.PotentialCombination(0, self.sorted_primes, result)
        comb_2 = aug9_2021.PotentialCombination(1, self.sorted_primes, result)
        comb_1.next_comb()

        heapq.heappush(comb_heap, comb_1)
        heapq.heappush(comb_heap, comb_2)
        self.assertEqual(4, comb_heap[0].product)
