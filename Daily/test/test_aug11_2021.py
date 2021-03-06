import math
import unittest

from Daily.src import aug11_2021


class TestOverall(unittest.TestCase):
    def setUp(self) -> None:
        self.test_subject = aug11_2021.number_of_arithmetic_slices

    def perform_simple_test(self, nums, answer):
        result = self.test_subject(nums)
        self.assertEqual(answer, result)

    def test_simple_case_1(self):
        nums = [2, 4, 6, 8, 10]
        answer = 7
        self.perform_simple_test(nums, answer)

    def test_simple_case_2(self):
        nums = [7, 7, 7, 7, 7]
        answer = 16
        self.perform_simple_test(nums, answer)

    def test_simple_case_3(self):
        nums = [1, 2, 3, 4, 5, 6]
        answer = 12
        self.perform_simple_test(nums, answer)

    def test_simple_case_4(self):
        nums = [0, 1, 2, 2, 2]
        # [0,1,2] [0,1,2] [0,1,2] (using different '2's) and [2,2,2]
        answer = 4
        self.perform_simple_test(nums, answer)

    def test_long_case_1(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        n_ss = len(nums)
        answer = sum(math.comb(n_ss, i) for i in range(3, n_ss + 1))
        self.perform_simple_test(nums, answer)

    def test_long_case_2(self):
        nums = [79, 20, 64, 28, 67, 81, 60, 58, 97, 85, 92, 96, 82, 89, 46, 50, 15, 2, 36, 44, 54, 2, 90, 37, 7, 79, 26,
                40, 34, 67, 64, 28, 60, 89, 46, 31, 9, 95, 43, 19, 47, 64, 48, 95, 80, 31, 47, 19, 72, 99, 28, 46, 13,
                9, 64, 4, 68, 74, 50, 28, 69, 94, 93, 3, 80, 78, 23, 80, 43, 49, 77, 18, 68, 28, 13, 61, 34, 44, 80, 70,
                55, 85, 0, 37, 93, 40, 47, 47, 45, 23, 26, 74, 45, 67, 34, 20, 33, 71, 48, 96]
        n_ss = len(nums)
        answer = sum(math.comb(n_ss, i) for i in range(3, n_ss + 1))
        self.perform_simple_test(nums, answer)


class TestForwardDistanceMatrixGeneration(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = aug11_2021.generate_forward_distance_matrix

    def test_simple_case_1(self):
        nums = [2, 4, 6, 7, 8]
        result = self.generator(nums)
        answer = [[-1, 2, 4, 5, 6], [-1, -1, 2, 3, 4], [-1, -1, -1, 1, 2], [-1, -1, -1, -1, 1], [-1, -1, -1, -1, -1]]
        self.assertListEqual(answer, result)

    def test_can_use_generated_matrix(self):
        nums = [2, 4, 6, 7, 8]
        result = self.generator(nums)
        self.assertEqual(4, result[0][2])
        self.assertEqual(2, result[2][4])


class TestFindLongestSlices(unittest.TestCase):
    def setUp(self) -> None:
        self.slices_finder = aug11_2021.find_longest_slices
        self.generator = aug11_2021.generate_forward_distance_matrix

    def test_simple_case_1(self):
        # nums = [2, 4, 6, 7, 8]
        distance_matrix = [[-1, 2, 4, 5, 6], [-1, -1, 2, 3, 4], [-1, -1, -1, 1, 2], [-1, -1, -1, -1, 1],
                           [-1, -1, -1, -1, -1]]
        first = 0
        second = 1
        result = self.slices_finder(distance_matrix, first, second)
        answer = [[0, 1, 2, 4], [0, 1, 2], [0, 1], [0]]
        self.assertListEqual(answer, result)

    def test_simple_case_2(self):
        # nums = [2, 4, 6, 7, 8]
        distance_matrix = [[-1, 2, 4, 5, 6], [-1, -1, 2, 3, 4], [-1, -1, -1, 1, 2], [-1, -1, -1, -1, 1],
                           [-1, -1, -1, -1, -1]]
        first = 2
        second = 3
        result = self.slices_finder(distance_matrix, first, second)
        answer = [[2, 3, 4], [2, 3], [2]]
        self.assertListEqual(answer, result)

    def test_use_generator_case_3(self):
        nums = [2, 4, 6, 8, 8, 8, 8]
        distance_matrix = self.generator(nums)
        first = 3
        second = 4
        result = self.slices_finder(distance_matrix, first, second)
        answer = [[3, 4, 5, 6], [3, 4, 5], [3, 4], [3, 4, 6], [3, 4], [3]]
        self.assertListEqual(answer, result)


class TestFindAllLongSlices(unittest.TestCase):
    def setUp(self) -> None:
        self.find_all_long_slices = aug11_2021.find_all_long_slices
        self.check_already_considered = aug11_2021.already_considered

    def test_simple_case_1(self):
        nums = [2, 4, 6, 7, 8]
        result = self.find_all_long_slices(nums)
        answer = {(0, 2): [[0, 1, 2, 4], [0, 1, 2]], (1, 2): [[1, 2, 4]], (2, 1): [[2, 3, 4]]}
        self.assertDictEqual(answer, result)
        pass

    def test_simple_case_2(self):
        nums = [2, 4, 6, 8, 10]
        result = self.find_all_long_slices(nums)
        answer_0_2 = [[0, 1, 2, 3, 4], [0, 1, 2, 3], [0, 1, 2]]
        self.assertListEqual(answer_0_2, result[(0, 2)])
        pass

    def test_simple_case_3(self):
        nums = [7, 7, 7, 7]
        result = self.find_all_long_slices(nums)
        answer_0_0 = [[0, 1, 2, 3], [0, 1, 2], [0, 1, 3], [0, 2, 3]]
        self.assertListEqual(answer_0_0, result[(0, 0)])
        pass


class TestAlreadyConsidered(unittest.TestCase):
    def setUp(self) -> None:
        self.check_already_considered = aug11_2021.already_considered

    def test_already_considered_case_1(self):
        arithmetic_slices_table = {(0, 2): [[0, 1, 2, 4]], (2, 1): [[2, 3, 4]]}
        first = 1
        d = 2
        self.assertTrue(self.check_already_considered(first, d, arithmetic_slices_table))

    def test_already_considered_case_2(self):
        arithmetic_slices_table = {(0, 2): [[0, 1, 2, 4]], (2, 1): [[2, 3, 4]]}
        first = 0
        d = 1
        self.assertFalse(self.check_already_considered(first, d, arithmetic_slices_table))

    def test_already_considered_case_3(self):
        arithmetic_slices_table = {(0, 2): [[0, 1, 2, 4]], (2, 1): [[2, 3, 4]]}
        first = 2
        d = 1
        self.assertTrue(self.check_already_considered(first, d, arithmetic_slices_table))


class TestDFS(unittest.TestCase):
    def setUp(self) -> None:
        self.dfs = aug11_2021.dfs_to_find_longest_slices
        self.dist_matrix_generator = aug11_2021.generate_forward_distance_matrix

    def test_simple_case_1(self):
        nums = [0, 1, 1, 1, 2]
        distance_matrix = self.dist_matrix_generator(nums)
        start = 0
        d = 1
        result = list(filter(lambda xs: len(xs) > 2, self.dfs(start, distance_matrix, d)))
        answer = [[0, 1, 4], [0, 2, 4], [0, 3, 4]]
        self.assertListEqual(answer, result)

    def test_simple_case_2(self):
        nums = [7, 7, 7, 7]
        distance_matrix = self.dist_matrix_generator(nums)
        start = 0
        d = 0
        result = list(filter(lambda xs: len(xs) > 2, self.dfs(start, distance_matrix, d)))
        answer = [[0, 1, 2, 3], [0, 1, 2], [0, 1, 3], [0, 2, 3]]
        self.assertListEqual(answer, result)

    def test_simple_case_3(self):
        nums = [7, 7, 7, 7, 7]
        distance_matrix = self.dist_matrix_generator(nums)
        start = 0
        d = 0
        result = list(filter(lambda xs: len(xs) > 2, self.dfs(start, distance_matrix, d)))
        answer = [[0, 1, 2, 3, 4], [0, 1, 2, 3], [0, 1, 2], [0, 1, 2, 4], [0, 1, 2], [0, 1, 3, 4], [0, 1, 3], [0, 1, 4],
                  [0, 2, 3, 4], [0, 2, 3], [0, 2, 4], [0, 3, 4]]
        self.assertListEqual(answer, result)

    def test_simple_case_4(self):
        nums = [7, 7, 7, 7, 7, 7]
        distance_matrix = self.dist_matrix_generator(nums)
        start = 0
        d = 0
        result = list(filter(lambda xs: len(xs) > 2, self.dfs(start, distance_matrix, d)))
        answer = [[0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4], [0, 1, 2, 3], [0, 1, 2, 3, 5], [0, 1, 2, 3], [0, 1, 2],
                  [0, 1, 2, 4, 5], [0, 1, 2, 4], [0, 1, 2], [0, 1, 2, 5], [0, 1, 2], [0, 1, 3, 4, 5], [0, 1, 3, 4],
                  [0, 1, 3], [0, 1, 3, 5], [0, 1, 3], [0, 1, 4, 5], [0, 1, 4], [0, 1, 5], [0, 2, 3, 4, 5], [0, 2, 3, 4],
                  [0, 2, 3], [0, 2, 3, 5], [0, 2, 3], [0, 2, 4, 5], [0, 2, 4], [0, 2, 5], [0, 3, 4, 5], [0, 3, 4],
                  [0, 3, 5], [0, 4, 5]]
        self.assertListEqual(answer, result)
