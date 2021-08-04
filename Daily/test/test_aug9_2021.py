import math
import unittest
from Daily.src import aug9_2021


class TestListChoose(unittest.TestCase):
    def test_1C1(self):
        nums = [1]
        result = aug9_2021.list_choose_r(nums, 1)
        answer = [[1]]
        self.assertListEqual(answer, result)

    def test_2C1(self):
        n = 2
        r = 1
        nums = [i for i in range(n)]
        result = aug9_2021.list_choose_r(nums, r)
        self.assertEqual(len(result), math.comb(n, r))

    def test_3C2(self):
        n = 3
        r = 2
        nums = [i for i in range(n)]
        result = aug9_2021.list_choose_r(nums, r)
        self.assertEqual(len(result), math.comb(n, r))

    def test_4C3(self):
        n = 4
        r = 3
        nums = [i for i in range(n)]
        result = aug9_2021.list_choose_r(nums, r)
        self.assertEqual(len(result), math.comb(n, r))


class TestTriangle(unittest.TestCase):
    def test_can_distinguish_bad_triangle(self):
        self.assertFalse(aug9_2021.is_triangle([1, 2, 3]))

    def test_can_distinguish_bad_triangle_case2(self):
        self.assertFalse(aug9_2021.is_triangle([1, 1, 3]))

    def test_can_pass_good_triangle(self):
        self.assertTrue(aug9_2021.is_triangle([1, 3, 3]))


class TestOverall(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 2, 3, 4]
        result = aug9_2021.triangle_number(nums)
        answer = 3
        self.assertEqual(result, answer)

    def test_case_2(self):
        nums = [66, 38, 74, 79, 52, 14, 17, 44, 57, 82, 43, 92, 53, 73, 30, 29, 48, 32, 0, 52, 36, 36, 92, 59, 38, 67,
                40, 68,
                54, 63, 26, 78, 67, 17, 43, 30, 18, 5, 81, 45, 66, 81, 82, 57, 88, 3, 12, 68, 43, 38, 91, 13, 48, 14,
                85, 22,
                33, 66, 7, 65, 74, 13, 62, 17, 69, 31, 1, 51, 22, 53, 75, 45, 70, 50, 65, 38, 56, 26, 60, 21, 24, 32,
                12, 0, 7,
                77, 67, 100, 85, 49, 83, 79, 76, 79, 76, 97, 44, 79, 4, 27]
        result = aug9_2021.triangle_number(nums)
        print(result)
