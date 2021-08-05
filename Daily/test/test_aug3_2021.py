import unittest
from Daily.src import aug3_2021


class TestAll(unittest.TestCase):
    def test_min_unsorted(self):
        nums = [2, 6, 4, 8, 10, 9, 15]
        result = aug3_2021.find_unsorted_subarray(nums)
        answer = 5
        self.assertEqual(answer, result)

    def test_min_unsorted_case2(self):
        nums = [1, 2, 3, 4]
        result = aug3_2021.find_unsorted_subarray(nums)
        answer = 0
        self.assertEqual(answer, result)

    def test_min_unsorted_case3(self):
        nums = [6, 5, 4, 3, 2, 1]
        result = aug3_2021.find_unsorted_subarray(nums)
        answer = 6
        self.assertEqual(answer, result)

    def test_min_unsorted_case4(self):
        nums = [3, 5, 4, 1, 2, 6]
        result = aug3_2021.find_unsorted_subarray(nums)
        answer = 5
        self.assertEqual(answer, result)

    def test_mono_increasing_short(self):
        nums = [1]
        result = aug3_2021.find_mono_increasing(nums)
        answer = 0
        self.assertEqual(answer, result)

    def test_mono_increasing_long(self):
        nums = [1, 2, 3, 4, 5, 0]
        result = aug3_2021.find_mono_increasing(nums)
        answer = 4
        self.assertEqual(answer, result)

    def test_find_front_max(self):
        nums = [1, 2, 3, 4, 5, 0]
        result = aug3_2021.find_front_max(nums)
        answer = -1
        self.assertEqual(answer, result)

    def test_find_front_max_case2(self):
        nums = [1, 2, 3, 6, 5, 4]
        result = aug3_2021.find_front_max(nums)
        answer = 2
        self.assertEqual(answer, result)

    def test_find_front_max_case3(self):
        nums = [1, 7, 3, 5, 6, 4]
        result = aug3_2021.find_front_max(nums)
        answer = 0
        self.assertEqual(answer, result)

    def test_find_back_min_case1(self):
        nums = [1, 7, 3, 5, 6, 4]
        result = aug3_2021.find_back_min(nums)
        answer = 6
        self.assertEqual(answer, result)

    def test_find_back_min_case2(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = aug3_2021.find_back_min(nums)
        answer = 0
        self.assertEqual(answer, result)

    def test_find_back_min_case3(self):
        nums = [4, 2, 3, 1, 5, 6]
        result = aug3_2021.find_back_min(nums)
        answer = 4
        self.assertEqual(answer, result)
