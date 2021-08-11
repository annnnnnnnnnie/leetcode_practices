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


class TestForwardDistanceMatrixGeneration(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = aug11_2021.generate_forward_distance_matrix

    def test_simple_case_1(self):
        nums = [2, 4, 6, 7, 8]
        result = self.generator(nums)
        answer = [[0, 2, 4, 5, 6], [0, 0, 2, 3, 4], [0, 0, 0, 1, 2], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
        self.assertListEqual(answer, result)

    def test_can_use_generated_matrix(self):
        nums = [2, 4, 6, 7, 8]
        result = self.generator(nums)
        self.assertEqual(4, result[0][2])
        self.assertEqual(2, result[2][4])


class TestFindLongestSlice(unittest.TestCase):
    def setUp(self) -> None:
        self.slice_finder = aug11_2021.find_longest_slice
        self.generator = aug11_2021.generate_forward_distance_matrix

    def test_simple_case_1(self):
        nums = [2, 4, 6, 7, 8]
        distance_matrix = [[0, 2, 4, 5, 6], [0, 0, 2, 3, 4], [0, 0, 0, 1, 2], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
        first = 0
        second = 1
        result = self.slice_finder(distance_matrix, first, second)
        answer = [0, 1, 2, 4]
        self.assertListEqual(answer, result)

    def test_simple_case_2(self):
        nums = [2, 4, 6, 7, 8]
        distance_matrix = [[0, 2, 4, 5, 6], [0, 0, 2, 3, 4], [0, 0, 0, 1, 2], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
        first = 2
        second = 3
        result = self.slice_finder(distance_matrix, first, second)
        answer = [2, 3, 4]
        self.assertListEqual(answer, result)

    def test_use_generator_case_3(self):
        nums = [2, 4, 6, 8, 8, 8, 8]
        distance_matrix = self.generator(nums)
        first = 3
        second = 4
        result = self.slice_finder(distance_matrix, first, second)
        answer = [3, 4, 5, 6]
        self.assertListEqual(answer, result)


class TestFindAllLongSlices(unittest.TestCase):
    def setUp(self) -> None:
        self.find_all_long_slices = aug11_2021.find_all_long_slices
        self.check_already_considered = aug11_2021.already_considered

    def test_simple_case_1(self):
        nums = [2, 4, 6, 7, 8]
        result = self.find_all_long_slices(nums)
        answer = {(0, 2): [0, 1, 2, 4], (2, 1): [2, 3, 4]}
        self.assertDictEqual(answer, result)
        pass

    def test_already_considered_case_1(self):
        arithmetic_slices_table = {(0, 2): [0, 1, 2, 4], (2, 1): [2, 3, 4]}
        first = 1
        d = 2
        self.assertTrue(self.check_already_considered(first, d, arithmetic_slices_table))
