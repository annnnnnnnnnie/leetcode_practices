import unittest

import Daily.src.jan2_2022


class TestOverall(unittest.TestCase):
    def setUp(self) -> None:
        self.last_remaining = Daily.src.jan2_2022.last_remaining
        self.answers = [-1, 1, 2, 2, 2, 2, 4, 4, 6, 6, 8, 8, 6, 6, 8, 8, 6, 6, 8, 8, 6, 6, 8, 8, 14, 14, 16, 16, 14, 14,
                        16, 16, 22, 22, 24, 24, 22, 22, 24, 24, 30, 30, 32, 32, 30, 30, 32, 32, 22, 22, 24, 24, 22, 22,
                        24, 24, 30, 30, 32, 32, 30, 30, 32, 32, 22, 22, 24, 24, 22, 22, 24, 24, 30, 30, 32, 32, 30, 30,
                        32, 32, 22, 22, 24, 24, 22, 22, 24, 24, 30, 30, 32, 32, 30, 30, 32, 32, 54, 54, 56, 56]

    def test_case_one(self):
        n = 1
        result = self.last_remaining(n)
        answer = 1
        self.assertEqual(answer, result)

    def test_case_two(self):
        n = 2
        result = self.last_remaining(n)
        answer = 2
        self.assertEqual(answer, result)

    def test_case_three(self):
        n = 3
        result = self.last_remaining(n)
        answer = 2
        self.assertEqual(answer, result)

    def test_case_four(self):
        n = 4
        result = self.last_remaining(n)
        answer = 2
        self.assertEqual(answer, result)

    def test_case_six(self):
        n = 6
        result = self.last_remaining(n)
        answer = 4
        self.assertEqual(answer, result)

    def test_all_cases_within_hundred(self):
        for i in range(1, len(self.answers)):
            n = i
            result = self.last_remaining(n)
            answer = self.answers[i]
            self.assertEqual(answer, result)
