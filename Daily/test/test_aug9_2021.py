import math
import unittest
from Daily.src import aug9_2021

long_nums = [66, 38, 74, 79, 52, 14, 17, 44, 57, 82, 43, 92, 53, 73, 30, 29, 48, 32, 0, 52, 36, 36, 92, 59, 38, 67,
             40, 68,
             54, 63, 26, 78, 67, 17, 43, 30, 18, 5, 81, 45, 66, 81, 82, 57, 88, 3, 12, 68, 43, 38, 91, 13, 48, 14,
             85, 22,
             33, 66, 7, 65, 74, 13, 62, 17, 69, 31, 1, 51, 22, 53, 75, 45, 70, 50, 65, 38, 56, 26, 60, 21, 24, 32,
             12, 0, 7,
             77, 67, 100, 85, 49, 83, 79, 76, 79, 76, 97, 44, 79, 4, 27]

long_nums_2 = [23, 28, 1, 94, 30, 70, 93, 57, 81, 13, 26, 92, 80, 60, 98, 13, 69, 77, 45, 7, 85, 66, 82, 19, 58, 75, 28,
               16, 85, 66, 55, 61, 92, 42, 77, 88, 60, 90, 14, 43, 75, 80, 70, 65, 77, 97, 18, 40, 75, 46, 81, 49, 51,
               24, 89, 29, 69, 14, 69, 66, 95, 70, 34, 83, 79, 87, 35, 9, 70, 55, 96, 100, 52, 40, 19, 4, 56, 78, 97, 3,
               56, 98, 30, 0, 58, 14, 76, 89, 71, 76, 82, 41, 10, 42, 53, 44, 87, 73, 78, 46]

long_nums_3 = [15, 44, 16, 43, 47, 47, 45, 27, 46, 2, 28, 12, 49, 22, 36, 12, 6, 48, 28, 19, 18, 34, 46, 38, 42, 3, 21,
               3, 54, 35, 21, 54, 13, 46, 50, 23, 53, 43, 5, 48, 40, 48, 10, 31, 15, 35, 50, 8, 48, 55, 52, 18, 54, 16,
               35, 4, 43, 55, 34, 13, 5, 13, 27, 41, 19, 22, 21, 26, 48, 4, 15, 1, 45, 51, 13, 49, 22, 33, 18, 18, 52,
               27, 6, 41, 7, 11, 48, 17, 37, 31, 42, 3, 45, 22, 6, 45, 42, 5, 28, 39, 35, 30, 24, 21, 49, 49, 47, 54,
               28, 42, 40, 26, 47, 8, 28, 1, 44, 4, 45, 23, 49, 53, 12, 48, 16, 27, 36, 21, 18, 41, 43, 9, 55, 27, 37,
               41, 5, 43, 12, 45, 0, 34, 19, 48, 14, 22, 43, 14, 13, 38, 15, 7, 41, 8, 37, 13, 45, 31, 47, 38, 45, 38,
               50, 44, 20, 40, 39, 38, 26, 29, 24, 10, 30, 23, 53, 38, 39, 3, 37, 4, 15, 22, 29, 4, 5, 4, 4, 19, 35, 30,
               30, 49, 16, 32, 36, 26, 37, 53, 46, 28, 24, 13, 12, 29, 2, 36, 21, 19, 15, 11, 22, 10, 30, 29, 40, 14,
               17, 39, 36, 17, 23, 39, 13, 29, 51, 8, 55, 10, 10, 47, 39, 1, 46, 27, 18, 7, 49, 38, 27, 14, 26, 35, 5,
               46, 54, 12, 18, 30, 11, 6, 29, 52, 44, 38, 51, 22, 26, 24, 41, 13, 39, 27, 0, 36, 38, 7, 37, 7, 9, 25, 4,
               8, 52, 33, 46, 33, 42, 43, 17, 23, 20, 23, 41, 8, 47, 16, 48, 46, 35, 35, 24, 0, 17, 12, 40, 52, 11, 16,
               7, 33, 6, 21, 30, 32, 55, 52, 52, 28, 11, 35, 39, 15, 27, 47, 52, 0, 11, 41, 50, 10, 13, 10, 5, 40, 21,
               0, 27, 12, 39, 20, 27, 39, 19, 28, 5, 51, 45, 19, 3, 1, 15, 53, 31, 45, 36, 33, 22, 4, 22, 20, 30, 7, 54,
               13, 19, 48, 32, 13, 38, 9, 4, 22, 26, 22, 43, 5, 47, 14, 15, 21, 15, 48, 10, 15, 47, 22, 9, 52, 4, 16,
               22, 47, 9, 13, 44, 15, 5, 19, 2, 55, 36, 49, 25, 52, 21, 5, 19, 46, 2, 51, 45, 12, 54, 47, 47, 23, 17,
               26, 52, 36, 49, 4, 42, 18, 20, 22, 47, 18, 37, 28, 19, 11, 21, 13, 37, 51, 2, 43, 36, 43, 0, 40, 50, 27,
               40, 41, 31, 41, 53, 2, 17, 4, 35, 52, 22, 25, 21, 16, 5, 41, 54, 5, 40, 3, 38, 12, 10, 53, 48, 28, 9, 7,
               46, 28, 3, 9, 44, 29, 39, 3, 41, 15, 29, 30, 47, 21, 12, 27, 53, 7, 34, 53, 53, 50, 53, 23, 46, 52, 40,
               21, 3, 46, 49, 17, 14, 36, 10, 54, 51, 22, 25, 34, 49, 49, 26, 45, 45, 17, 30, 19, 6, 49, 41, 9, 19, 25,
               51, 23, 55, 11, 0, 1, 13, 26, 15, 41, 38, 19, 51, 21, 11, 8, 55, 25, 21, 15, 18, 15, 48, 4, 37, 36, 5,
               45, 13, 13, 16, 26, 0, 41, 8, 51, 20, 38, 28, 46, 3, 37, 52, 6, 24, 11, 18, 39, 25, 48, 16, 41, 50, 44,
               48, 7, 29, 14, 15, 28, 7, 46, 15, 16, 46, 20, 35, 6, 27, 10, 17, 1, 42, 30, 37, 41, 37, 52, 55, 4, 6, 17,
               27, 33, 45, 37, 11, 29, 16, 42, 33, 39, 35, 33, 30, 25, 37, 6, 25, 22, 43, 31, 42, 25, 15, 27, 19, 15,
               10, 1, 45, 24, 23, 17, 17, 33, 12, 53, 30, 44, 30, 2, 30, 8, 45, 49, 48, 46, 52, 13, 41, 29, 46, 39, 50,
               51, 19, 55, 36, 29, 23, 8, 11, 49, 43, 45, 51, 2, 41, 53, 6, 38, 52, 26, 45, 0, 55, 14, 42, 25, 10, 4,
               39, 5, 47, 42, 55, 37, 35, 53, 14, 27, 54, 41, 19, 34, 38, 43, 22, 41, 23, 12, 13, 17, 36, 23, 41, 15,
               34, 24, 44, 21, 3, 25, 10, 14, 43, 16, 35, 45, 1, 22, 26, 20, 5, 8, 37, 42, 47, 1, 2, 33, 2, 21, 8, 36,
               50, 6, 45, 40, 48, 16, 12, 1, 55, 0, 53, 51, 35, 19, 14, 3, 21, 33, 2, 54, 33, 2, 18, 53, 34, 19, 23, 32,
               27, 39, 13, 48, 27, 12, 7, 50, 16, 49, 35, 27, 12, 29, 6, 34, 7, 18, 50, 6, 49, 24, 1, 18, 53, 27, 36, 0,
               37, 42, 51, 12, 38, 8, 29, 38, 11, 24, 4, 2, 15, 19, 1, 25, 9, 30, 50, 30, 8, 15, 50, 52, 25, 8, 29, 44,
               7, 41, 30, 45, 9, 23, 20, 49, 15, 16, 48, 34, 10, 44, 52, 22, 4, 6, 2, 8, 23, 13, 39, 7, 31, 29, 4, 35,
               43, 2, 33, 34, 24, 41, 38, 47, 5, 38, 28, 34, 1, 44, 14, 13, 12, 8, 6, 0, 24, 9, 4, 39, 37, 32, 18, 38,
               15, 29, 14, 11, 40, 34, 12, 16, 7, 7, 50, 18, 24, 30, 15, 13, 41, 42, 47, 22, 17, 14, 38, 46, 45, 22, 12,
               12, 12, 25, 11, 24, 41, 8, 51, 51, 25, 46, 15, 13, 47, 38, 20, 0, 21, 7, 30, 49, 42, 43, 53, 24, 19, 17,
               46, 50, 15, 33, 1, 42, 14, 55, 26, 17, 41, 39, 23, 46, 35, 39, 16, 16, 37, 50, 38, 24, 20, 32, 51, 22,
               53, 50, 10, 39, 4, 2, 27, 1, 25, 18, 40, 50, 9, 35, 37, 27, 37, 39, 29, 2, 38, 32, 6, 30, 32, 4, 43, 46,
               21, 9, 40, 45, 49, 34, 37, 4, 55, 19, 47, 3, 42, 33, 13, 43, 3, 3, 22, 49]


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
        self.assertEqual(math.comb(len(nums), r), len(result))

    def test_3C2(self):
        n = 3
        r = 2
        nums = [i for i in range(n)]
        result = aug9_2021.list_choose_r(nums, r)
        self.assertEqual(math.comb(len(nums), r), len(result))

    def test_4C3(self):
        n = 4
        r = 3
        nums = [i for i in range(n)]
        result = aug9_2021.list_choose_r(nums, r)
        self.assertEqual(math.comb(len(nums), r), len(result))

    def test_10C3(self):
        n = 10
        r = 3
        nums = [i for i in range(n)]
        result = aug9_2021.list_choose_r(nums, r)
        self.assertEqual(math.comb(len(nums), r), len(result))


class TestListChooseDP(unittest.TestCase):
    def test_4C3(self):
        n = 4
        r = 3
        nums = [i for i in range(n)]
        result = aug9_2021.list_choose_r_fast(nums, r)
        self.assertEqual(math.comb(len(nums), r), len(result))

    def test_a_lot_C_3(self):
        nums = long_nums
        r = 3
        result = aug9_2021.list_choose_r_fast(nums, r)
        self.assertEqual(math.comb(len(nums), r), len(result))

    def test_a_lot_C_3_case2(self):
        nums = long_nums_2
        r = 3
        result = aug9_2021.list_choose_r_fast(nums, r)
        self.assertEqual(len(result), math.comb(len(nums), r))


class TestIsTriangle(unittest.TestCase):
    def test_can_distinguish_bad_triangle(self):
        self.assertFalse(aug9_2021.is_triangle([1, 2, 3]))

    def test_can_distinguish_bad_triangle_case2(self):
        self.assertFalse(aug9_2021.is_triangle([1, 1, 3]))

    def test_can_pass_good_triangle(self):
        self.assertTrue(aug9_2021.is_triangle([1, 3, 3]))


class TestCombMethod(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 2, 3, 4]
        result = aug9_2021.triangle_number_comb(nums)
        answer = 3
        self.assertEqual(answer, result)

    def test_case_2(self):
        nums = long_nums
        result = aug9_2021.triangle_number_comb(nums)
        answer = 87446
        self.assertEqual(answer, result)

    def test_case_3(self):
        nums = long_nums_2
        result = aug9_2021.triangle_number_comb(nums)
        answer = 98993
        self.assertEqual(answer, result)


class TestForLoopMethod(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 2, 3, 4]
        result = aug9_2021.triangle_number_loop(nums)
        answer = 3
        self.assertEqual(answer, result)

    def test_case_2(self):
        nums = long_nums
        result = aug9_2021.triangle_number_loop(nums)
        answer = 87446
        self.assertEqual(answer, result)

    def test_case_3(self):
        nums = long_nums_2
        result = aug9_2021.triangle_number_loop(nums)
        answer = 98993
        self.assertEqual(answer, result)


class TestBinarySearch(unittest.TestCase):
    def test_search_4_elems(self):
        sorted_nums = [1, 2, 3, 4]
        max_length_exclusive = 3
        start = 0
        end = len(sorted_nums)
        result = aug9_2021.binary_search(sorted_nums, max_length_exclusive, start, end)
        answer = 1
        self.assertEqual(answer, result)

    def test_search_middle(self):
        sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8]
        max_length_exclusive = 6
        start = 2
        end = len(sorted_nums)
        result = aug9_2021.binary_search(sorted_nums, max_length_exclusive, start, end)
        answer = 4
        self.assertEqual(answer, result)


class TestBinaryMethod(unittest.TestCase):
    test_subject = aug9_2021.triangle_number_binary

    def test_case_1(self):
        nums = [2, 2, 3, 4]
        result = TestBinaryMethod.test_subject(nums)
        answer = 3
        self.assertEqual(answer, result)

    def test_case_2(self):
        nums = [2] * 10
        result = TestBinaryMethod.test_subject(nums)
        answer = math.comb(len(nums), 3)
        self.assertEqual(answer, result)

    def test_case_3(self):
        nums = [2] * 100 + [3] * 100
        result = TestBinaryMethod.test_subject(nums)
        answer = math.comb(len(nums), 3)
        self.assertEqual(answer, result)

    def test_case_4(self):
        nums = [1, 1, 5]
        result = TestBinaryMethod.test_subject(nums)
        answer = 0
        self.assertEqual(answer, result)

    def test_case_5(self):
        nums = [1, 2, 2, 5]
        result = TestBinaryMethod.test_subject(nums)
        answer = 1
        self.assertEqual(answer, result)

    def test_case_6(self):
        nums = long_nums
        result = TestBinaryMethod.test_subject(nums)
        answer = 87446
        self.assertEqual(answer, result)

    def test_case_7(self):
        nums = long_nums_2
        result = TestBinaryMethod.test_subject(nums)
        answer = 98993
        self.assertEqual(answer, result)

    def test_case_8(self):
        nums = [0, 1, 1, 1]
        result = TestBinaryMethod.test_subject(nums)
        answer = 1
        self.assertEqual(answer, result)
