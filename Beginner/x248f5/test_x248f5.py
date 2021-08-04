import unittest
from x248f5 import Solution


class Tests(unittest.TestCase):
    def test_no_dup(self):
        nums = [1, 2, 3, 4, 5]
        self.assertFalse(Solution.contains_duplicates(nums))

    def test_dup(self):
        nums = [1, 2, 3, 4, 5, 3]
        self.assertTrue(Solution.contains_duplicates(nums))