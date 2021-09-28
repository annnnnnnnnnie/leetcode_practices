import unittest

from Daily.src import sep28_2021
from Daily.src.sep28_2021 import TreeNode


def get_input_tree1():
    llt = TreeNode(3, TreeNode(3), TreeNode(2))
    lrt = TreeNode(2, None, TreeNode(1))
    lt = TreeNode(5, llt, lrt)
    rt = TreeNode(-3, None, TreeNode(11))
    t = TreeNode(10, lt, rt)
    return t


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.path_sum = sep28_2021.path_sum
        self.input_tree_1 = get_input_tree1()

    def test_find_n_path_small_1(self):
        t = self.input_tree_1
        target_sum = 8
        result = self.path_sum(t, target_sum)
        answer = 3
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
