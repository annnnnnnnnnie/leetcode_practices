import unittest

from Beginner.x2jrse import x2jrse


class TestOverall(unittest.TestCase):
    def setUp(self) -> None:
        self.two_sum_finder = x2jrse.two_sum

    def test_simple_case_1(self):
        nums = [3, 2, 4]
        target = 6
        result = self.two_sum_finder(nums, target)
        answer = [1, 2]
        self.assertSetEqual(set(answer), set(result))
