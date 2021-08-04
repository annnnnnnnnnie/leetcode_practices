import unittest
from functools import reduce
from operator import mul

import xw8dz6


class Testing(unittest.TestCase):
    def test_generate_one_level(self):
        nums = [1, 2, 3, 4]
        result = xw8dz6.Solution.generate_one_level(nums)

        answer = [2, 12]
        self.assertListEqual(result, answer)

    def test_generate_one_level_odd(self):
        nums = [1, 2, 3, 4, 5]
        result = xw8dz6.Solution.generate_one_level(nums)

        answer = [2, 12, 5]
        self.assertListEqual(result, answer)

    def test_can_generate_product_tree(self):
        nums = [1, 2, 3, 4, 5, 6]
        pt = xw8dz6.Solution.generate_product_tree(nums)

        answer = [[1, 2, 3, 4, 5, 6], [2, 12, 30], [24, 30]]
        self.assertListEqual(pt, answer)

    def test_can_output_something(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = xw8dz6.Solution.product_except_self(nums)
        self.assertTrue(len(result) > 0)


class TestProductTree(unittest.TestCase):
    def test_small_product_tree_print(self):
        pt = xw8dz6.ProductTree.singleton(1, 10)
        printed = pt.__str__()
        self.assertIn("Leaf 1", printed)

    def test_product_tree_print(self):
        lt = xw8dz6.ProductTree.singleton(1, 10)
        rt = xw8dz6.ProductTree.singleton(2, 20)
        pt = xw8dz6.ProductTree.from_lt_rt(lt, rt)
        printed = pt.__str__()
        self.assertIn("node", printed)

    def test_build_product_trees(self):
        nums = [1, 2, 3, 4, 5]
        pts = [xw8dz6.ProductTree.singleton(i, nums[i]) for i in range(len(nums))]
        self.assertTrue(len(pts) > 0)

    def test_build_pt_from_nums(self):
        nums = [1, 2, 3, 4, 5]
        pts = [xw8dz6.ProductTree.singleton(i, nums[i]) for i in range(len(nums))]
        pt = xw8dz6.Solution.build_product_tree(pts)
        self.assertTrue(len(pts) > 0)

    def test_product_of_one(self):
        nums = [1, 2, 3, 4, 5]
        pt = xw8dz6.Solution.generate_product_tree(nums)
        i = 0
        result = xw8dz6.Solution.product_of_one(i, pt)
        answer = reduce(mul, nums[(i + 1):])
        self.assertEqual(result, answer)

    def test_product_of_many(self):
        nums = [1, 2, 3, 4, 5]
        pt = xw8dz6.Solution.generate_product_tree(nums)
        for i in range(len(nums)):
            result = xw8dz6.Solution.product_of_one(i, pt)
            answer = reduce(mul, nums) // nums[i]
            self.assertEqual(result, answer)
