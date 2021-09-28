# https://leetcode-cn.com/problems/path-sum-iii/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class PossibleSumsTree:
    def __init__(self, val=0, left=None, right=None, possible_sums=None):
        if possible_sums is None:
            possible_sums = []
        self.val = val
        self.left = left
        self.right = right
        self.possible_sums = possible_sums

    def __str__(self):
        return f"Node {self.val} {self.possible_sums}"


def path_sum(root, target_sum):
    possible_sums_tree = compute_possible_sums_tree(root)
    count = compute_n_paths(possible_sums_tree, target_sum)
    return count


def compute_n_paths(root: PossibleSumsTree, target_sum):
    if root:
        cur = root.possible_sums.count(target_sum)
        return cur + compute_n_paths(root.left, target_sum) + compute_n_paths(root.right, target_sum)
    else:
        return 0


def compute_possible_sums_tree(root: TreeNode):
    if root:
        possible_sums = [root.val]
        lt = compute_possible_sums_tree(root.left)

        if lt:
            possible_sums.extend(map(lambda n: n + root.val, lt.possible_sums))
        rt = compute_possible_sums_tree(root.right)

        if rt:
            possible_sums.extend(map(lambda n: n + root.val, rt.possible_sums))

        return PossibleSumsTree(root.val, lt, rt, possible_sums)
    else:
        return None


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        return path_sum(root, targetSum)
