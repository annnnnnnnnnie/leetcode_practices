import unittest
from x2skh7 import Solution


class Tests(unittest.TestCase):
    def test_rotate_zero(self):
        nums = [1, 2, 3, 4, 5]
        answer = [1, 2, 3, 4, 5]
        step = 0
        Solution.rotate(nums, step)

        self.assertListEqual(nums, answer)

    def test_rotate_one(self):
        nums = [1, 2, 3, 4, 5]
        answer = [5, 1, 2, 3, 4]
        step = 1
        Solution.rotate(nums, step)

        self.assertListEqual(nums, answer)

    def test_rotate_two(self):
        nums = [1, 2, 3, 4]
        answer = [3, 4, 1, 2]
        step = 2
        Solution.rotate(nums, step)

        self.assertListEqual(nums, answer)

    def test_rotate_small(self):
        nums = [1, 2]
        answer = [2, 1]
        step = 1
        Solution.rotate(nums, step)

        self.assertListEqual(nums, answer)

    def test_rotate_four(self):
        nums = [1, 2, 3, 4, 5, 6]
        answer = [3, 4, 5, 6, 1, 2]
        step = 4
        Solution.rotate(nums, step)

        self.assertListEqual(nums, answer)
