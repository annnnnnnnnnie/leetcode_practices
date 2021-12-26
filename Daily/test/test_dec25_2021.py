import unittest

import Daily.src.dec25_2021
from Daily.src.dec25_2021 import TreeNode


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.bf_walk = Daily.src.dec25_2021.convert_tree_to_list
        self.is_odd_even_tree = Daily.src.dec25_2021.is_even_odd_tree

    def test_expand_small_tree(self):
        lt = TreeNode(1)
        rt = TreeNode(2)
        root = TreeNode(0, lt, rt)
        result = self.bf_walk(root)
        vals = list(map(lambda ts: list(map(lambda node: node.val, ts)), result))
        answer = [[0], [1, 2]]
        self.assertListEqual(answer, vals)

    def test_expand_partially_filled_tree(self):
        lt = TreeNode(1)
        rt = None
        root = TreeNode(0, lt, rt)
        result = self.bf_walk(root)
        vals = list(map(lambda ts: list(map(lambda node: node.val, ts)), result))
        answer = [[0], [1]]
        self.assertListEqual(answer, vals)

    def test_all_odd_nums_list_is_all_odd(self):
        ns = [2 * i + 1 for i in range(10)]
        self.assertTrue(Daily.src.dec25_2021.is_all_odd(ns))
        ns = []
        self.assertTrue(Daily.src.dec25_2021.is_all_odd(ns))

    def test_not_all_odd_nums_list_is_not_all_odd(self):
        ns = [2 * i + 1 for i in range(10)] + [2]
        self.assertFalse(Daily.src.dec25_2021.is_all_odd(ns))

    def test_all_even(self):
        ns = [2 * i for i in range(10)]
        self.assertTrue(Daily.src.dec25_2021.is_all_even(ns))
        ns = []
        self.assertTrue(Daily.src.dec25_2021.is_all_even(ns))
        ns = [2 * i for i in range(10)] + [1]
        self.assertFalse(Daily.src.dec25_2021.is_all_even(ns))

    def test_strictly_increasing(self):
        ns = [i for i in range(10)]
        self.assertTrue(Daily.src.dec25_2021.is_increasing(ns))
        ns = []
        self.assertTrue(Daily.src.dec25_2021.is_increasing(ns))
        ns = [i for i in range(10)] * 2
        self.assertFalse(Daily.src.dec25_2021.is_increasing(ns))
        ns = [i for i in range(10)] + [9]
        self.assertFalse(Daily.src.dec25_2021.is_increasing(ns))

    def test_case_1(self):
        root = TreeNode(1,
                        TreeNode(10, TreeNode(3,
                                              TreeNode(12),
                                              TreeNode(8)),
                                 None),
                        TreeNode(4, TreeNode(7,
                                             TreeNode(6)),
                                 TreeNode(9,
                                          TreeNode(2))))
        result = self.is_odd_even_tree(root)
        self.assertTrue(result)

    def test_case_3(self):
        root = TreeNode(5,
                        TreeNode(9, TreeNode(3),
                                 TreeNode(5)),
                        TreeNode(1, TreeNode(7)))
        result = self.is_odd_even_tree(root)
        self.assertFalse(result)

        if __name__ == '__main__':
            unittest.main()
