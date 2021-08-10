import unittest

from Daily.src import aug10_2021


class TestOverall(unittest.TestCase):
    def setUp(self) -> None:
        self.test_subject = aug10_2021.number_of_arithmetic_slices

    def test_small_case_1(self):
        nums = [1, 2, 3, 4]
        result = self.test_subject(nums)
        answer = 3
        self.assertEqual(answer, result)

    def test_edge_case_1(self):
        nums = [1]
        result = self.test_subject(nums)
        answer = 0
        self.assertEqual(answer, result)

    def test_large_case_1(self):
        n = 5000
        nums = [0 for _ in range(n)]
        result = self.test_subject(nums)
        answer = sum([i for i in range(n - 1)])
        self.assertEqual(answer, result)
