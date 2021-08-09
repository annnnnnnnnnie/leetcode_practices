import unittest

from Beginner.x21ib6 import x21ib6


class TestOverall(unittest.TestCase):
    def setUp(self) -> None:
        self.test_subject = x21ib6.single_number

    def test_single_number_easy_1(self):
        nums = [2, 2, 1]
        result = self.test_subject(nums)
        answer = 1
        self.assertEqual(answer, result)

    def test_single_number_easy_2(self):
        nums = [4, 1, 2, 1, 2]
        result = self.test_subject(nums)
        answer = 4
        self.assertEqual(answer, result)
